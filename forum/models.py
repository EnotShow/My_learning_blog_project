from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Статус публикация")
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    # comm = models.ForeignKey('Comment', unique=False, on_delete=models.CASCADE, blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Названия категории')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['pk']

    def get_absolute_url(self):
        return reverse('cat', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name

# TODO: add related_name='+'
# TODO: ManyToOneField ?
# class Comment(models.Model):
#     user = models.OneToOneField(User, models.CASCADE, verbose_name='Пользователь')
#     content = models.CharField(max_length=500, verbose_name='Текст комментария')
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
#     time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
#
#     class Meta:
#         verbose_name = 'Комментарии'
#         verbose_name_plural = 'Комментарии'
#         ordering = ['pk']
#
#     def __str__(self):
#         return self.content[:50]
