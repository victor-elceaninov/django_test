from django.conf import settings
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey('Category', related_name='articles',
                                 on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255, null=False)
    description = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Category(models.Model):
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='users',
                             on_delete=models.CASCADE)
    article = models.ForeignKey('Article',
                                related_name='likes',
                                on_delete=models.CASCADE)
