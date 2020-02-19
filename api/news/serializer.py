from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Articles, Categories


class ArticleSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    is_liked = serializers.SerializerMethodField(read_only=True)
    link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Articles
        fields = ('id',
                  'category_id',
                  'title',
                  'slug',
                  'short_description',
                  'description',
                  'posted',
                  'link',
                  'likes',
                  'is_liked',
                  )

    def get_likes(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return obj.likes.filter(user=user).exists()

    def get_link(self, obj):
        return reverse("news:article-detail",
                       kwargs={"version": "v1", 'pk': obj.id},
                       request=self.context.get('request'))


class CategorySerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_total(category):
        return category.articles.count()

    class Meta:
        model = Categories
        fields = ('id', 'title', 'description', 'total')
