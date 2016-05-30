from django import forms

from books.models import Book,Chapter,Comment      
        
class Book_Form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name','book_author','book_year','book_pages','book_publisher','book_ISBN','book_content','book_image']

#    def __init__(self, *args, **kwargs):
#        super(Book_Form, self).__init__(*args, **kwargs)
#        self.fields['book_image'].required = False


class Chapter_Form(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_index','chapter_content']
        
class Comment_Form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']
        
#    def __init__(self, *args, **kwargs):
#        super(Comment_Form, self).__init__(*args, **kwargs)
#        self.fields['comment_user'].required = False