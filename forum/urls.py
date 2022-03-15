from .views import *

from django.urls import path

urlpatterns = [
    # path('', NoneView.as_view(), name='home')
    path('', IndexView.as_view(), name='home'),
    # path('<slug:post_slug>', CategoryListView.as_view(), name='cat'),
    path('about/', NoneView.as_view(), name='about'),
    path('support/', NoneView.as_view(), name='support'),
    path('post/<slug:post_slug>', PostView.as_view(), name='post')
]
