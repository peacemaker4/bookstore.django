from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs["class"]='form-control'
        self.fields["author"].widget.attrs["class"]='form-control'
        self.fields["publisher"].widget.attrs["class"]='form-control'
        self.fields["summary"].widget.attrs["class"]='form-control'

        self.fields["title"].widget.attrs["class"]='Название'
        self.fields["author"].widget.attrs["class"]='Автор'

    class Meta:
        model=Book
        fields="__all__"
