from django.shortcuts import render
from books.models import Book, Genre

def landing(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    return render(request, 'landing/index.html', {
        'books': books,
        'books_count': books.count(),
        'filter_books_count': books.count(),
        'genres': genres,
    })

def filter(request, genre_slug):
    genre=Genre.objects.get(slug=genre_slug)
    books=genre.book_set.all()
    genres = Genre.objects.all()
    return render(request, 'landing/index.html', {
        'books': books,
        'books_count': Book.objects.count(),
        'filter_books_count': books.count(),
        'genres': genres,
    })