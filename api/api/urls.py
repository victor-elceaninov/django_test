from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/auth/login/', LoginView.as_view(), name='login'),
    re_path('api/(?P<version>(v1|v2))/auth/register/', RegisterView.as_view(), name='register'),
    re_path('api/(?P<version>(v1|v2))/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('api/(?P<version>(v1|v2))/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path('api/(?P<version>(v1|v2))/', include('news.urls', namespace='news')),
]