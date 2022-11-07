import pytest
from django.test.client import Client
from rest_framework import status

from ...accounts.models import CustomUser
from ...accounts.tests.factories import UserFactory
from ...organizations.models import OrganizationUser
from ...organizations.tests.factories import OrganizationFactory
from ..models import Service, ServiceNotify
from .factories import ServiceFactory


@pytest.mark.django_db
class TestServicesViewSet:
    URL = "/api/v1/services/"

    def test_unauthorized(self, client: Client):
        res = client.get(self.URL)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_list(self, client: Client, user: CustomUser):
        """ """

        other_user = UserFactory.create()
        organization_1 = OrganizationFactory.create(owner=user)
        organization_2 = OrganizationFactory.create(owner=other_user)
        organization_3 = OrganizationFactory.create(owner=other_user)

        ServiceFactory.create_batch(2, organization=organization_1)
        ServiceFactory.create_batch(2, organization=organization_2)
        ServiceFactory.create_batch(2, organization=organization_3)

        OrganizationUser.objects.create(
            organization_id=organization_2.id, user_id=user.id, is_accepted=True
        )
        OrganizationUser.objects.create(
            organization_id=organization_3.id, user_id=user.id, is_accepted=False
        )

        client.force_login(user)
        res = client.get(self.URL)
        assert res.status_code == status.HTTP_200_OK
        data = res.json()
        assert data.__len__() == 4
