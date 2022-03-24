from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .forms import *

menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Support', 'url_name': 'support'},
        {'title': 'About Us', 'url_name': 'about'},
        {'title': 'Add post', 'url_name': 'addpost'}]

no_auth = [{'title': 'Log in', 'url_name': 'login'},
           {'title': 'Sign up', 'url_name': 'signup'}]


class PostListView(ListView):
    model = Post
    paginate_by = 6

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


class PostDetailView(FormMixin, DetailView):
    model = Post

    template_name = 'forum/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        context['u'] = 'addpost'
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        else:
            return HttpResponse('No access')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')

class CategoryListView(ListView):
    model = Post
    paginate_by = 6

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


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User

    template_name = 'forum/profile.html'

    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context


class UserView(TemplateView):
    model = User

    template_name = 'forum/user.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostForm

    template_name = "forum/addpost.html"
    context_object_name = 'form'

    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['auth'] = no_auth
        context['title'] = 'MyForum'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect('home')


class NoneView(TemplateView):
    template_name = "forum/test.html"
