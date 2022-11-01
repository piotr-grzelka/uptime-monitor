from typing import Sequence, Type

from rest_framework import permissions
from rest_framework.authentication import BaseAuthentication
from rest_framework.throttling import AnonRateThrottle


class AnonApiView:
    """
    Base view configuration for anonymous user
    """

    permission_classes = [permissions.AllowAny]
    throttle_classes = [AnonRateThrottle]
    authentication_classes: Sequence[Type[BaseAuthentication]] = []
