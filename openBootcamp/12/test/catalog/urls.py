# from django.shortcuts import render
# from django.conf.urls import url
from django.urls import include, re_path
from . import views
# from catalog import views
# from django.conf.urls import url
# create your views here.
urlpatterns = [
    re_path(r'^$', views.index, name='index')
    # url(r"^/$", views.index, name="index"),
    
]
