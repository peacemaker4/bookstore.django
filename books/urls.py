from django.urls import path
from books import views

urlpatterns = [
    path('', views.AllBooks.as_view(), name="books"),
    path('search', views.FindBooks.as_view(), name="searchbooks"),
    # path('<int:id>', views.BookPage.as_view(), name="details"),
    path('<int:id>', views.details, name="details"),
    path('<int:id>/update', views.BookUpdate.as_view(), name="update"),
    path('<int:id>/delete', views.BookDelete.as_view(), name="delete"),
    path('addbook', views.AddBook.as_view(), name="createbook"),
]