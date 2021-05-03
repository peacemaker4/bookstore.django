from django.db import models
from django.urls import reverse
from django.utils import timezone

class Book(models.Model):
    title=models.CharField(verbose_name="Название", max_length=200)
    author=models.CharField(verbose_name="Автор", max_length=200)
    publisher=models.CharField(verbose_name="Издатель", max_length=200)
    summary = models.TextField(verbose_name="Содержание")
    genre=models.ManyToManyField('Genre', null=True, blank=True, default=None)
    cover=models.ImageField(verbose_name="Обложка",null=True, blank=True)
    bookfile=models.FileField(verbose_name="Файл", null=True, blank=True)
    published_at = models.DateTimeField(verbose_name = "Дата публикации", auto_now_add=timezone.now())
    def __str__(self):
        return f'Book: {self.title}'
    class Meta:
        verbose_name='Книга'
        verbose_name_plural='Библиотека'
    def get_absolute_url(self):
        return reverse("details", args=[self.id])
class Genre(models.Model):
    genre=models.CharField(verbose_name="Жанр", max_length=200)
    slug=models.SlugField(verbose_name="Слаг",db_index=True, max_length=255)
    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'
    def __str__(self):
        return f'Жанр: {self.genre}'

# class Rate(models.Model):
#     rating=models.CharField(verbose_name='Оценка', max_length=12)
#     comment = models.TextField(verbose_name="Комментарий")

