from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'categories', CategoryViewSet, basename='category')

app_name = 'news'
urlpatterns = router.urls
