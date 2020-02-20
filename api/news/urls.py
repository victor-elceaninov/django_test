from django.urls import path
from .views import ArticlesView, ArticleDetailView, CategoriesDetailView, \
    ArticleLikeView

app_name = 'news'
urlpatterns = [
    path('news/articles', ArticlesView.as_view(), name='articles'),
    path('news/categories', CategoriesDetailView.as_view(), name='categories'),
    path('news/article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('news/article/<int:pk>/like', ArticleLikeView.as_view(), name='article-like'),
]
