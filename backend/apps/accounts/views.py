from dateutil.parser import parse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from .models import CustomUser
from ..contrib.views import AnonApiView
from .serializers import UserRegisterConfirmSerializer, UserRegisterSerializer
from django.core.signing import Signer, BadSignature
from django.utils.timezone import now


class RegisterView(CreateAPIView, AnonApiView):
    """
    User registration view
    """

    serializer_class = UserRegisterSerializer


class RegisterConfirmView(GenericAPIView, AnonApiView):
    """
    User register confirm view
    """

    serializer_class = UserRegisterConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data.get('token')
        print(">>", token)

        try:
            unsigned = Signer().unsign_object(token)
            user_id = unsigned['id']
            valid_to = parse(unsigned['valid_to'])
        except BadSignature:
            raise ValidationError({"token": _("Provided token is malformed.")})

        if valid_to < now():
            raise ValidationError({"token": _("Provided token is expired.")})

        user: CustomUser = get_object_or_404(CustomUser, pk=user_id)

        if user.is_verified:
            raise ValidationError({"token": _("User already confirmed.")})

        user.is_verified = True
        user.save()

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
