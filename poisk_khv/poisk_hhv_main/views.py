

from django import views


from django.shortcuts import render, get_object_or_404


from .models import AboutDocs, AboutPartner, AboutUs, ActiveTeam, Article, CatImages,   OurTeam, Post, Projects, Smi
# Create your views here.


def articles(request):
    article = Article.objects.all()
    return render(request, "articles.html", {'article': article})


def article_detail(request, project_id):
    articles = get_object_or_404(Article, pk=project_id)
    return render(request, "article_detail.html", {"articles": articles})


# def article(request):
#     article = Article.objects.all()

#     return render(request, "article.html", {"article": article})


def gallery(request):
    cat_img = CatImages.objects.all()

    return render(request, "gallery.html", {"cat_img": cat_img})


def gallery_detail(request, gallery_id):
    gallery_photos = get_object_or_404(CatImages, pk=gallery_id)
    return render(request, "gallery_detail.html", {"gallery_photos": gallery_photos})


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

# это переделать


def our_team(request):
    our_team = OurTeam.objects.all()
    active_team = ActiveTeam.objects.all()
    return render(request, "our_team.html", {"our_team": our_team, 'active_team': active_team})


def about_us(request):
    partners = AboutPartner.objects.all()
    docs = AboutDocs.objects.all()
    about_us = AboutUs.objects.all()
    context = {"about_us": about_us, 'docs': docs, 'partners': partners}
    return render(request, 'about_us.html', context)


def about_us_detail(request, item_id):
    item = get_object_or_404(AboutUs, pk=item_id)
    return render(request, "about_us_detail.html", {"item": item})


def projects(request):
    projects = Projects.objects.all()
    return render(request, "projects.html", {'projects': projects})


def project_detail(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, "project_detail.html", {"project": project})
