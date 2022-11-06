from django.db.models.query_utils import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Organization
from .permissions import OrganizationPermission
from .serializers import OrganizationSerializer


class OrganizationsViewSet(ModelViewSet):
    """
    Organizations, list, view and manage
    """

    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, OrganizationPermission]

    def get_queryset(self):
        """
        Filter objects by ownership and other users privileges for current logged in user
        """
        user_id = self.request.user.id
        query = Q(owner_id=user_id) | Q(users__user_id=user_id, users__is_accepted=True)
        return Organization.objects.filter(query)
