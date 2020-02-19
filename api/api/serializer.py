from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    EmailField,
)
from rest_framework_simplejwt.serializers import PasswordField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )


class TokensSerializer(Serializer):
    refresh = CharField(max_length=255)
    access = CharField(max_length=255)


class UserLoginSerializer(Serializer):
    user = UserSerializer()
    tokens = TokensSerializer()


class UserCreateSerializer(ModelSerializer):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    password = PasswordField(min_length=8, required=True, )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        )

    @staticmethod
    def validate_email(value):
        user = User.objects.filter(email=value)
        if user.exists():
            raise ValidationError("This email is already taken.")
        return value

    def create(self, validated_data) -> User:
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]

        user = User(first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email)
        user.set_password(password)
        user.save()
        return user
