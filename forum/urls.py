from .views import *

from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', NoneView.as_view(), name='about'),
    path('support/', NoneView.as_view(), name='support'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='cat'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user/<slug:user_slug>/', NoneView.as_view(), name='user'),
    path('addpost/', PostCreateView.as_view(), name='addpost'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup', UserCreateView.as_view(), name='signup'),
    path('logout', logout_user, name='logout'),
]
