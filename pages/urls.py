# page/urls.py
from django.urls import path
from .views import Homepageview

app_name = 'pages'

urlpatterns = [
    path('', Homepageview.as_view(), name = 'home')
]