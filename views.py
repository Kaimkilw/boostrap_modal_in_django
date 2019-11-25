from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book
from boostrap_moderl_forms.generic import (
	BSModalCreateView,
	BSModalUpdateView,

	)
from django.views import generic
from .forms import BookForm

class Index(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'


class BookCreateView(BSModalCreateView):
    template_name = 'app/create_book.html'
    form_class = BookForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')

class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'app/update_book.html'
    form_class = BookForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('index')
