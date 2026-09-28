from .views import PostListView, PostDetailView
from django.urls import path

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog/<slug:post_slug>/', PostDetailView.as_view(), name='post_url')
]
