from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserCreateSerializer, UserLoginSerializer


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    """
    @api {post} /auth/login Login
    @apiName Login
    @apiGroup User
    @apiVersion 1.0.0
    @apiUse UserLogin 
    """

    def post(self, request, *args, **kwargs):
        user = authenticate(request,
                            username=request.data.get("username", ""),
                            password=request.data.get("password", ""))
        if user is not None:
            return Response(data=login_a_user(request, user),
                            status=status.HTTP_200_OK)

        raise NotAuthenticated("These credentials do not match our records.")


class RegisterView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    """
    @api {post} /auth/register Registration
    @apiName Registration
    @apiGroup User
    @apiVersion 1.0.0
    @apiUse UserRegister
    """

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)

            return Response(data=login_a_user(request, user),
                            status=status.HTTP_201_CREATED)


def login_a_user(request, user):
    # login saves the User’s ID in the session,
    # using Django’s session framework.
    login(request, user)
    refresh = RefreshToken.for_user(user)
    result = UserLoginSerializer(
        {
            "user": user,
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        }
    )

    return result.data
