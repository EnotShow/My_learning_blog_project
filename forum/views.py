from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import *
from .forms import *

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Support', 'url_name': 'support'},
        {'title': 'About Us', 'url_name': 'about'},
        {'title': 'Add post', 'url_name': 'addpost'}]

no_auth = [{'title': 'Log in', 'url_name': 'login'},
           {'title': 'Sign up', 'url_name': 'signup'}]


class PostListView(ListView):
    model = Post

    template_name = 'forum/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post

    template_name = 'forum/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        context['u'] = 'addpost'
        return context


class CategoryListView(ListView):
    model = Post

    template_name = "forum/index.html"
    context_object_name = 'posts'
    slug_url_kwarg = 'cat_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs.get('cat_slug'))


class UserCreateView(CreateView):
    form_class = SignUpForm

    template_name = 'forum/usersignup.html'
    context_object_name = 'form'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context


class UserLoginView(LoginView):
    form_class = AuthForm

    template_name = 'forum/userlogin.html'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context

    def get_success_url(self):
        return reverse_lazy('home')


class ProfileView(ListView):
    model = User

    template_name = 'forum/profile.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = AddPostForm

    template_name = "forum/addpost.html"
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context


def logout_user(request):
    logout(request)
    return redirect('home')


class NoneView(TemplateView):
    template_name = "forum/test.html"
