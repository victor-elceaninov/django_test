from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Articles, Categories, Likes
from .serializer import ArticleSerializer, CategorySerializer


class ArticlesView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Articles.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            try:
                category = int(category_id)
            except ValueError:
                raise ValidationError({'category_id': ['Invalid value type.']})
            else:
                queryset = queryset.filter(category_id=category)

        return queryset.order_by('id')

    """
    @api {get} /news/articles Articles
    @apiVersion 1.0.0
    @apiGroup News
    @apiUse Articles
    """

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleDetailView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer

    """
    @api {get} /news/article/:id Article
    @apiVersion 1.0.0
    @apiName Article Details
    @apiGroup News
    @apiUse Article
    """

    def get(self, request, *args, **kwargs):
        try:
            article = self.queryset.get(pk=kwargs["pk"])
            return Response(self.get_serializer(article).data)
        except Articles.DoesNotExist:
            raise Http404("Article with id: {} does not exist".format(
                kwargs["pk"]))


class CategoriesDetailView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    """
    @api {get} /news/categories Categories/Category
    @apiVersion 1.0.0
    @apiGroup News
    @apiUse Categories
    """

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleLikeView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Articles.objects.all()

    """
    @api {post} /news/article/:id/like Like/Unlike
    @apiVersion 1.0.0
    @apiGroup News
    @apiUse LikeUnlike
    """

    def post(self, request, *args, **kwargs):
        try:
            user = request.user
            article = self.queryset.get(pk=kwargs['pk'])
            like, is_created = Likes.objects.get_or_create(
                user=user,
                article=article
            )

            if is_created is False:
                Likes.objects.filter(
                    user=request.user,
                    article=article
                ).delete()
                return Response({'message': 'You have unliked current article!'},
                                status=status.HTTP_200_OK)

            return Response({'message': 'You have liked current article!'},
                                status=status.HTTP_200_OK)
        except Articles.DoesNotExist:
            raise Http404()
