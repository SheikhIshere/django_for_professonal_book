from django.urls import path
from .views import (
    BookListView, 
    BookDetailsView,
    SearchResultsListView,
)
urlpatterns = [
    path('', BookListView.as_view(), name = 'book_list'),
    path('<uuid:pk>/', BookDetailsView.as_view(), name = 'book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results')
]