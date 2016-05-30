# -*- coding: utf-8 -*-

from django import forms

from movies.models import Movie,Comment
        
class Movie_Form(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name','movie_director','movie_writers','movie_stars','movie_year','movie_content','movie_image']

#    def __init__(self, *args, **kwargs):
#        super(Movie_Form, self).__init__(*args, **kwargs)
#        self.fields['movie_image'].required = False

class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']