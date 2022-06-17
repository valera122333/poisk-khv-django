from django.urls import path

from .views import *
from .import views


urlpatterns = [



    path('smi/', views.smi_about, name='smi_about'),
    path('', views.home, name='home'),
    path("project/<int:post_id>", views.post_detail, name="post_detail"),
    path('contact', views.contact, name='contact'),

    path('our_team/', views.our_team, name='our_team'),
    path('about_us/', views.about_us, name='about_us'),
    path("about_us/<int:item_id>",
         views.about_us_detail, name="about_us_detail"),
    path('projects/', views.projects, name='projects'),
    path("project_detail/<int:project_id>",
         views.project_detail, name="project_detail"),
    path('gallery/', views.gallery, name='gallery'),
    path("gallery_detail/<int:gallery_id>",
         views.gallery_detail, name="gallery_detail"),
    path('articles/', views.articles, name='articles'),

    path("article_detail/<int:project_id>",
         views.article_detail, name="article_detail"),
]
