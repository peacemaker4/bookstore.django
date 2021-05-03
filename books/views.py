from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.models import Book, Genre
from books.forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class HomePage(LoginRequiredMixin,TemplateView):
    template_name="library/index.html"
    login_url='/authentication/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books_count"] = Book.objects.count()
        context["genres_count"] = Genre.objects.count()
        context["books_covers"] = Book.objects.all().order_by('-id').exclude(cover__exact='')[:10]

        context["recents"] = Book.objects.all().order_by('-id')[:5]
        return context

class AllBooks(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name="library/books.html"
    fields='__all__'
    model=Book

    login_url='/authentication/login'
    permission_required = "auth.change_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()

        context["recents"] = Book.objects.all().order_by('-id')[:5]
        context["forms"]=BookForm()
        return context
class FindBooks(LoginRequiredMixin, ListView):
    template_name="library/search.html"
    fields='__all__'
    model=Book

    login_url='/authentication/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()

        return context
class AddBook(LoginRequiredMixin, CreateView):
    template_name="library/create.html"
    fields='__all__'
    model=Book

    login_url='/authentication/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forms"]=BookForm()
        return context

# class BookPage(LoginRequiredMixin, DetailView):
#     template_name="library/bookpage.html"
#     model=Book
#     pk_url_kwarg="id"
#     login_url='/authentication/login'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

@login_required(login_url='/authentication/login')
def details(request, id):
    book=Book.objects.get(pk=id)
    genres=Book.objects.get(pk=id).genre.values_list('slug','genre')
    genreslist=[]
    for g in genres:
        genreslist.append({
        "slug": g[0],
        "genre": g[1],
        })
    genres=genreslist

    return render(request, 'library/bookpage.html', {
        'book':book,
        'genres':genres
    })


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Book
    template_name="library/update.html"
    form_class=BookForm
    pk_url_kwarg="id"
    login_url='/authentication/login'

    permission_required = "auth.change_user"

class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model=Book
    pk_url_kwarg="id"
    success_url="/books/"
    login_url='/authentication/login'

    permission_required = "auth.change_user"
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

def handler403(request, exception):
    template_name="error/403.html"
    response = render(request, template_name)
    response.status_code = 403
    return response