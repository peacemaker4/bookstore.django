from django.contrib import admin
from books.models import Book, Genre

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','publisher','summary','published_at')
    list_filter=('title','author', 'publisher','published_at')
    search_fields=['title']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('genre','slug')
    list_filter=('genre','slug')
    search_fields=['genre']