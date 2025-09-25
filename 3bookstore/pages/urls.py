# page/urls.py
from django.urls import path
from .views import Homepageview, AboutPageView

app_name = 'pages'

urlpatterns = [
    path('', Homepageview.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name='about'),
]