# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from books import views

app_name = 'books'

urlpatterns = [
  url(r'^$', views.book_list, name='book_list'),
  url(r'^create/$', views.book_create, name='book_create'),
  url(r'^edit/(?P<pk>\d+)/$', views.book_update, name='book_edit'),
  url(r'^delete/(?P<pk>\d+)/$', views.book_delete, name='book_delete'),
  url(r'^detail/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
  url(r'^create_chapter/(?P<pk>\d+)/$', views.book_create_chapter, name='book_create_chapter'),
  url(r'^edit_chapter/(?P<book_pk>\d+)/(?P<chapter_pk>\d+)/$', views.book_update_chapter, name='book_edit_chapter'),
]