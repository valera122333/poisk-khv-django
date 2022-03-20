from django.urls import path

from .views import *
from .import views


urlpatterns = [



    path('smi/', views.smi_about, name='smi_about'),
    path('', views.home, name='home'),
    path("project/<int:post_id>", views.post_detail, name="post_detail"),
    path('contact', views.contact, name='contact'),
    path('reestr/', views.reestr, name='reestr'),

]
