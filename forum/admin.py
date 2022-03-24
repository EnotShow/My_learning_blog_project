from django.contrib import admin

from .models import *


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'photo', 'is_published')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'time_create')
