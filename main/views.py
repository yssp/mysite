from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from movies.models import Movie

def main_index(request):
    book_list = {}
    movie_list = {}
    search = request.GET.get('q')
    category = request.GET.get('sel1')
    if search == None or search == "":
        if request.session.has_key('search') and request.session.has_key('category'):
            search = request.session['search'] 
            category = request.session['category'] 
            
            del request.session['search']
            del request.session['category']
            request.session.modified = True
            
            if category == "书籍":
                book_list = Book.objects.filter(book_name__contains = search)
            elif category == "影视":
                movie_list = Movie.objects.filter(movie_name__contains = search) 
            else:
                book_list = Book.objects.filter(book_name__contains = search)
                movie_list = Movie.objects.filter(movie_name__contains = search) 
            
        else:
            if category == "书籍":
                book_list = Book.objects.all()[:6]
            elif category == "影视":
                movie_list = Movie.objects.all()[:6]
            else:
                book_list = Book.objects.all()[:6]
                movie_list = Movie.objects.all()[:6]
    else:
        if category == "书籍":
            book_list = Book.objects.filter(book_name__contains = search)
        elif category == "影视":
            movie_list = Movie.objects.filter(movie_name__contains = search) 
        else:
            book_list = Book.objects.filter(book_name__contains = search)
            movie_list = Movie.objects.filter(movie_name__contains = search) 
        
    data = {}
    data['book_list'] = book_list
    data['movie_list'] = movie_list
    return render(request, 'main/main_index.html', data)
    
def main_login(request):
    data = {}
    return render(request, 'main/main_index.html', data)
