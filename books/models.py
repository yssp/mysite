from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse

class Book(models.Model):
    book_name = models.CharField(max_length = 100)
    book_author = models.CharField(max_length = 100,null=True,blank=True)
    book_year = models.IntegerField(null=True,blank=True)
    book_pages = models.IntegerField(null=True,blank=True)
    book_publisher = models.CharField(max_length = 200,null=True,blank=True)
    book_ISBN = models.CharField(max_length = 200,null=True,blank=True)
    book_content = models.TextField()
    book_image = models.ImageField(upload_to='books/images',null=True,blank=True)
        
    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
        
class Chapter(models.Model):
    book = models.ForeignKey(Book)
    chapter_index = models.IntegerField()
    chapter_content = models.TextField()
    
    def __str__(self):
        return self.book.book_name + ' : ' + str(self.chapter_index)
    
class Comment(models.Model):
    book = models.ForeignKey(Book)
    comment_user = models.CharField(max_length = 100,default='游客',blank=True)
    comment_content = models.TextField()
    
    def __str__(self):
        return self.book.book_name + ' : ' + self.comment_user + ' : ' + self.comment_content