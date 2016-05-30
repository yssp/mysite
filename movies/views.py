from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from movies.models import Movie
from movies.forms import Movie_Form,Comment_Form

def movie_list(request):
    movies = Movie.objects.all()
    data = {}
    data['object_list'] = movies
    return render(request, 'movies/movie_list.html', data)

def movie_create(request):
    form = Movie_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movies:movie_list')
    return render(request, 'movies/movie_form.html', {'form':form})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = Movie_Form(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movies:movie_list')
    return render(request, 'movies/movie_form.html', {'form':form})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)    
    if request.method=='POST':
        movie.delete()
        return redirect('movies:movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'object':movie})
    
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = Comment_Form(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect(reverse('movies:movie_detail', args=(movie.id,)))
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
    data = {}
    data['movie'] = movie
    data['form'] = form
    return render(request, 'movies/movie_detail.html', data)