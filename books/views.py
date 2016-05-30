from django.shortcuts import render

# Create your views here.
    
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from books.models import Book,Chapter
from books.forms import Book_Form,Chapter_Form,Comment_Form

def book_list(request):
    books = Book.objects.all()
    data = {}
    data['object_list'] = books
    return render(request, 'books/book_list.html', data)

def book_create(request):
    form = Book_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form':form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = Book_Form(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form':form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)    
    if request.method=='POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'object':book})
    
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = Comment_Form(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return HttpResponseRedirect(reverse('books:book_detail', args=(book.id,)))
    elif request.method == "GET":
        if 'search_btn' in request.GET:
            search = request.GET.get('q')
            category = request.GET.get('sel1')  
            request.session['search'] = search
            request.session['category'] = category
            return HttpResponseRedirect(reverse('main:main_index', args=()))        
    else:
        pass

    form = Comment_Form()
    chapter = book.chapter_set.order_by('chapter_index')
    data = {}
    data['book'] = book
    data['chapter'] = chapter
    data['form'] = form
    return render(request, 'books/book_detail.html', data)
    
def book_create_chapter(request, pk):
    book = get_object_or_404(Book, pk=pk)  
    form = Chapter_Form(request.POST or None)
    if form.is_valid():
        chapter = form.save(commit=False)
        chapter.book = book
        chapter.save()
        return HttpResponseRedirect(reverse('books:book_detail', args=(book.id,)))
    return render(request, 'books/book_form.html', {'form':form})
    
def book_update_chapter(request, book_pk, chapter_pk):
    book = get_object_or_404(Book, pk=book_pk)
    chapter = get_object_or_404(Chapter, pk=chapter_pk)
    form = Chapter_Form(request.POST or None, instance=chapter)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('books:book_detail', args=(book.id,)))
    return render(request, 'books/book_form.html', {'form':form})