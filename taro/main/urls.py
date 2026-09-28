from .views import index, about
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
