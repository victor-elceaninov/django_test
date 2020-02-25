from django.http import Http404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Article, Category, Likes
from .serializer import ArticleSerializer, CategorySerializer
from api.filters import ArticlesFilterBackend


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = PageNumberPagination
    filter_backends = [ArticlesFilterBackend]
    filterset_fields = ['category_id']

    """
    @apiVersion 1.0.0
    @apiGroup News
    @apiUse ArticlesPage
    """

    @action(methods=['post'], detail=True,
            permission_classes=[permissions.IsAuthenticated],
            url_path='like', url_name='like')
    def set_like_unlike(self, request, pk=None, **kwargs):
        try:
            like, is_created = Likes.objects.get_or_create(
                user=request.user,
                article=self.get_queryset().get(pk=pk)
            )
        except ValueError as err:
            raise ValidationError({'id': [err]})
        except Article.DoesNotExist:
            raise Http404()
        else:
            if is_created is False:
                like.delete()
                return Response({'message': 'You have unliked current article!'},
                                status=status.HTTP_204_NO_CONTENT)
            return Response({'message': 'You have liked current article!'},
                            status=status.HTTP_201_CREATED)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = None
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'
    object = Category

    """
    @apiVersion 1.0.0
    @apiGroup News
    @apiUse CategoriesPage
    """

