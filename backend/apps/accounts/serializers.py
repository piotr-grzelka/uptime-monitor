from typing import Any

from django.contrib.auth import password_validation
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .emails import send_register_verification_email
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Standard user serializer
    """

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email")


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User register serializer
    """

    password = serializers.CharField(
        label=_("Password"), required=True, write_only=True
    )
    password_repeat = serializers.CharField(
        label=_("Repeat password"), required=True, write_only=True
    )

    def create(self, validated_data: Any):
        """Send a mail to newly created user"""

        del validated_data["password_repeat"]

        instance = CustomUser.objects.create_user(**validated_data)
        send_register_verification_email(self.context["request"], instance)
        return instance

    def validate(self, attrs):
        """Custom validation for password field"""
        tmp_user = CustomUser(
            first_name=attrs.get("first_name"),
            last_name=attrs.get("last_name"),
            email=attrs.get("email"),
        )
        password = attrs.get("password")

        errors = {}

        try:
            password_validation.validate_password(password=password, user=tmp_user)
        except exceptions.ValidationError as exc:
            errors["password"] = list(exc.messages)

        if attrs["password"] != attrs["password_repeat"]:
            errors["password_repeat"] = _("The passwords provided do not match.")

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(attrs)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password", "password_repeat")


class UserRegisterConfirmSerializer(serializers.Serializer):
    """
    User register confirm serializer
    """

    def create(self, validated_data):
        print(validated_data)

    def update(self, *args, **kwargs):
        pass

    token = serializers.CharField(label=_("Token"), required=True)
