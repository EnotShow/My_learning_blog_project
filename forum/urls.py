from .views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', NoneView.as_view(), name='about'),
    path('support/', NoneView.as_view(), name='support'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='cat'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user/<slug:username>/', UserView.as_view(), name='user'),
    path('addpost/', PostCreateView.as_view(), name='addpost'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup', UserCreateView.as_view(), name='signup'),
    path('logout', logout_user, name='logout'),
    path('profile/admin/', admin.site.urls, name='admin'),
]
