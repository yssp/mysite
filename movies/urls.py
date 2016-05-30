# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from movies import views

app_name = 'movies'

urlpatterns = [
  url(r'^$', views.movie_list, name='movie_list'),
  url(r'^create/$', views.movie_create, name='movie_create'),
  url(r'^edit/(?P<pk>\d+)/$', views.movie_update, name='movie_edit'),
  url(r'^delete/(?P<pk>\d+)/$', views.movie_delete, name='movie_delete'),
  url(r'^detail/(?P<pk>\d+)/$', views.movie_detail, name='movie_detail'),
]