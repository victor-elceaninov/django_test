from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'short_description', 'posted')
    list_filter = ('posted',)
    search_fields = ['title', 'short_description', 'description']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
