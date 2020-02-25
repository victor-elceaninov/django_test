from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Article, Category


class ArticleSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)
    link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'category_id', 'title', 'slug', 'short_description',
                  'description', 'posted', 'link', 'likes', 'is_liked')

    def get_likes(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return obj.likes.filter(user=user).exists()

    def get_link(self, obj):
        return get_url('article-detail', self.context, obj.id)


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)
    link = serializers.SerializerMethodField(read_only=True)
    articles = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_total(category):
        return category.articles.count()

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'link', 'articles', 'total')

    def get_link(self, obj):
        return get_url('category-detail', self.context, obj.id)

    def get_articles(self, obj):
        url = get_url('article-list', self.context)
        return '{}?category_id={}'.format(url, obj.id)


def get_url(name, context, pk=None):
    kwargs = {'version': 'v1'}
    if pk:
        kwargs['pk'] = pk
    return reverse(viewname='news:{}'.format(name),
                   kwargs=kwargs,
                   request=context.get('request'))
