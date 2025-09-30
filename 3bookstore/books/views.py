# books/views.py
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book
from django.contrib.auth.mixins import (
    PermissionRequiredMixin,
    LoginRequiredMixin
)


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'books_list' # if i don't use it i have to use object_list on the template page to ac access
    template_name = 'books/book_list.html'


class BookDetailsView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_details.html'
    login_url = 'accounts:signup'
    permission_required = 'books.speial_status' 