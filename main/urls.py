# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from main import views

app_name = 'main'

urlpatterns = [
  url(r'^$', views.main_index, name= 'main_index'),
  url(r'^login/$', views.main_login, name= 'main_login'),
]