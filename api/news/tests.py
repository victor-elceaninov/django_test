from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.utils import json

from .models import Articles, Categories


class BaseViewTest(APITestCase):
    client = APIClient()

    def login_client(self, username="", password=""):
        # get a token from DRF
        response = self.client.post(
            reverse("login", kwargs={"version": "v1"}),
            data=json.dumps({
                "username": username,
                "password": password,
            }),
            content_type='application/json'
        )
        self.token = response.data["tokens"]["access"]
        # set the token in the header
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token

    def setUp(self):
        self.category = Categories.objects.create(
            title="Category 1",
            slug="category-1",
        )
        self.article = Articles.objects.create(
            title="Article 1",
            slug="article-1",
            short_description="short description",
            description="description",
            category=self.category
        )
        self.user = User.objects.create_superuser(
            username="test_user2",
            email="test2@mail.com",
            password="testing",
            first_name="test",
            last_name="User",
        )


class GetAllArticlesTest(BaseViewTest):
    """
    This test ensures that permission is restricted for unauthorized User.
    Endpoint /news/articles
    """
    def test_news_index_not_authorized(self):
        response = self.client.get(
            reverse('news:articles', kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    """
    This test ensures that authorized User can view articles.
    Endpoint /news/articles
    """
    def test_news_index_authorized(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse('news:articles', kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArticleTest(BaseViewTest):
    """
    This test ensures that article exists.
    Endpoint /news/article/:id
    """
    def test_article_exists(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse("news:article-detail", kwargs={"version": "v1",
                                                   "pk": self.article.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This test ensures that article doesn't exists
    Endpoint /news/article/:id
    """
    def test_article_not_exists(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse("news:article-detail", kwargs={"version": "v1", "pk": 222})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    This test ensures that user can add like to an article.
    Endpoint /news/article/:id/like
    """
    def test_add_like_to_an_article(self):
        self.login_client('test_user2', 'testing')
        response = self.client.post(
            reverse("news:article-like", kwargs={"version": "v1",
                                                 "pk": self.article.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This test ensures that user can remove like to an article.
    Endpoint /news/article/:id/like
    """
    def test_remove_like_from_an_article(self):
        self.login_client('test_user2', 'testing')
        response = self.client.post(
            reverse("news:article-like", kwargs={"version": "v1",
                                                 "pk": self.article.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This test ensures that unauthorized User cann't view article detail page.
    Endpoint /news/articles
    """

    def test_article_not_authorized(self):
        response = self.client.get(
            reverse('news:article-detail', kwargs={"version": "v1",
                                                   "pk": self.article.id})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CategoriesTest(BaseViewTest):
    """
    This test ensures that permission is restricted for unauthorized User.
    Endpoint /news/categories
    """
    def test_categories_not_authorized(self):
        response = self.client.get(
            reverse("news:categories", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    """
    This test ensures that permission is restricted for authorized User.
    Endpoint /news/categories
    """
    def test_categories_authorized(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse("news:categories", kwargs={"version": "v1"})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PaginationFilteringTest(BaseViewTest):
    """
    This test ensures that string will not pass as value of page parameter.
    Endpoint /news/articles
    """
    def test_page_param_with_string_value(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse('news:articles', kwargs={"version": "v1"}),
            {"page": "asdasd"}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    """
    This test ensures that integer will pass as value of page parameter.
    Endpoint /news/articles
    """
    def test_page_param_with_int_value(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse('news:articles', kwargs={"version": "v1"}),
            {"page": 1}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    This test ensures that string will not pass as value of category_id 
    parameter.
    Endpoint /news/articles
    """
    def test_category_id_param_with_string_value(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse('news:articles', kwargs={"version": "v1"}),
            {"category_id": "asdasd"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    """
    This test ensures that integer will pass as value of category_id parameter.
    Endpoint /news/articles
    """
    def test_category_id_param_with_int_value(self):
        self.login_client('test_user2', 'testing')
        response = self.client.get(
            reverse('news:articles', kwargs={"version": "v1"}),
            {"category_id": self.category.id}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
