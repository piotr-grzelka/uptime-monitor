from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import Organization


class OrganizationPermission(BasePermission):
    """
    Object permissions for organization instance
    """

    def has_object_permission(
        self, request: Request, view: APIView, obj: Organization
    ) -> bool:
        """
        Only owner can manage organization instance
        """

        if request.method in SAFE_METHODS:
            return True

        return obj.owner.id == request.user.id
