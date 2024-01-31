from django.urls import path
from booksLanding import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('<slug:genre_slug>', views.filter, name="books.filter")
]
