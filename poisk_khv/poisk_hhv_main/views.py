from django.shortcuts import render
from django import views

from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Post, Smi
# Create your views here.


def home(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    context = {"posts": posts, "total_posts": total_posts}
    return render(request, "home.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})


def smi_about(request):
    smis = Smi.objects.all()
    return render(request, "smi_about.html", {"smis": smis})


def contact(request):
    return render(request, "contact.html")


def reestr(request):
    categorys = Category.objects.all()
    articles = Article.objects.order_by("title")
    context = {"categorys": categorys, "articles": articles}

    return render(request, "reestr.html", context)
