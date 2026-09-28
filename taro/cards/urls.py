from .views import CardsDeskListView,CardsDeskDetailView, CardDetailView
from django.urls import path

urlpatterns = [
    path('cards/', CardsDeskListView.as_view(), name='cards'),
    path('cards/<slug:desk_slug>/', CardsDeskDetailView.as_view(), name='card_url'),
    path('cards/<slug:desk_slug>/<slug:card_slug>/', CardDetailView.as_view()),
]
