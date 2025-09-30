# books/views.py
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books_list' # if i don't use it i have to use object_list on the template page to ac access
    template_name = 'books/book_list.html'


class BookDetailsView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_details.html'