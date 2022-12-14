from django.db.models.query_utils import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Service
from .serializers import ServiceSerializer


class ServicesViewSet(ModelViewSet):
    """
    Services, list, view and manage
    """

    serializer_class = ServiceSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        """
        Filter objects by ownership and other users privileges for current logged in user
        """
        user_id = self.request.user.id
        query = Q(organization__owner_id=user_id) | Q(
            organization__users__user_id=user_id, organization__users__is_accepted=True
        )
        return Service.objects.filter(query)
