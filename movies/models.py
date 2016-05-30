from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse

class Movie(models.Model):
    movie_name = models.CharField(max_length = 100)
    movie_year = models.IntegerField(null=True,blank=True)
    movie_content = models.TextField()
    movie_director = models.CharField(max_length = 100,null=True,blank=True)
    movie_writers = models.CharField(max_length = 100,null=True,blank=True)
    movie_stars = models.TextField(null=True,blank=True)
    movie_image = models.ImageField(upload_to='movies/images',null=True,blank=True)
        
    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('movie_edit', kwargs={'pk': self.pk})
        
class Comment(models.Model):
    movie = models.ForeignKey(Movie)
    comment_user = models.CharField(max_length = 100,default='游客',blank=True)
    comment_content = models.TextField()
    
    def __str__(self):
        return self.movie.movie_name + ' : ' + self.comment_user + ' : ' + self.comment_content
        