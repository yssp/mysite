from django.contrib import admin

# Register your models here.

from books.models import Book,Chapter,Comment

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Comment)