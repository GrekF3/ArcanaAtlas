from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):

    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        qs = Post.objects.all().order_by('-date_published')
        return qs
    


class PostDetailView(DetailView):
    model = Post
    template_name = "blogpost.html"
    context_object_name = 'post'
    slug_field = 'post_slug'
    slug_url_kwarg = 'post_slug'


