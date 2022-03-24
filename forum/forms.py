from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import *


class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'photo', 'cat', 'content']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
