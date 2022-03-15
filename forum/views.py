from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import *

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Support', 'url_name': 'support'},
        {'title': 'About Us', 'url_name': 'about'}]


class IndexView(ListView):
    model = Post

    template_name = 'forum/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'MyForum'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostView(DetailView):
    model = Post.objects.filter('pk')

    template_name = 'forum/post.html'
    context_object_name = 'post'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'MyForum'
        return context


class CategoryListView(ListView):
    model = Post

    template_name = "forum/test.html"

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs.get('slug'))


class NoneView(TemplateView):
    template_name = "forum/test.html"
