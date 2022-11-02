import pytest
from django.test.client import Client
from rest_framework import status

from ...accounts.models import CustomUser
from ...accounts.tests.factories import UserFactory
from ..models import Organization, OrganizationUser
from .factories import OrganizationFactory


@pytest.mark.django_db
class TestOrganizationsViewSet:
    URL = "/api/v1/organizations/"

    def test_unauthorized(self, client: Client):
        res = client.get(self.URL)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_list(self, client: Client, user: CustomUser):
        """
        only organizations with my ownership and other accepted access should be returned
        """

        other_user = UserFactory.create()
        OrganizationFactory.create_batch(2, owner=user)
        other_items = OrganizationFactory.create_batch(4, owner=other_user)

        OrganizationUser.objects.create(
            organization_id=other_items[0].id, user_id=user.id, is_accepted=True
        )
        OrganizationUser.objects.create(
            organization_id=other_items[0].id, user_id=user.id, is_accepted=False
        )

        client.force_login(user)
        res = client.get(self.URL)
        assert res.status_code == status.HTTP_200_OK
        data = res.json()
        assert data.__len__() == 3

    def test_retrieve_when_i_am_owner(self, client: Client, organization: Organization):
        client.force_login(organization.owner)
        res = client.get(f"{self.URL}{organization.id}/")
        assert res.status_code == status.HTTP_200_OK
        data = res.json()
        assert data.__len__() == 3

    def test_retrieve_when_i_am_user(
        self, client: Client, user: CustomUser, organization: Organization
    ):
        url = f"{self.URL}{organization.id}/"
        client.force_login(user)

        # without user organization instance
        res = client.get(url)
        assert res.status_code == status.HTTP_404_NOT_FOUND

        organization_user = OrganizationUser.objects.create(
            organization_id=organization.id, user_id=user.id, is_accepted=False
        )

        # with not accepted user organization instance
        res = client.get(url)
        assert res.status_code == status.HTTP_404_NOT_FOUND

        organization_user.is_accepted = True
        organization_user.save()

        # with accepted user organization instance
        res = client.get(url)
        assert res.status_code == status.HTTP_200_OK

    def test_update_when_i_am_owner(
        self, client: Client, user: CustomUser, organization: Organization
    ):
        client.force_login(organization.owner)
        old_owner_id = organization.owner.id

        res = client.put(
            f"{self.URL}{organization.id}/",
            {"name": "new nice name", "owner_id": user.id},
            content_type="application/json",
        )
        assert res.status_code == status.HTTP_200_OK

        organization.refresh_from_db()
        assert organization.name == "new nice name"
        assert organization.owner.id == old_owner_id  # owner can't be changed by update

    def test_update_when_i_am_not_an_owner(
        self, client: Client, user: CustomUser, organization: Organization
    ):
        client.force_login(user)

        OrganizationUser.objects.create(
            organization_id=organization.id, user_id=user.id, is_accepted=True
        )

        res = client.put(
            f"{self.URL}{organization.id}/",
            {
                "name": "new nice name",
            },
            content_type="application/json",
        )
        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_when_i_am_owner(
        self, client: Client, user: CustomUser, organization: Organization
    ):
        client.force_login(organization.owner)

        assert Organization.objects.count() == 1

        res = client.delete(f"{self.URL}{organization.id}/")
        assert res.status_code == status.HTTP_204_NO_CONTENT
        assert Organization.objects.count() == 0

    def test_delete_when_i_am_not_an_owner(
        self, client: Client, user: CustomUser, organization: Organization
    ):
        client.force_login(user)

        OrganizationUser.objects.create(
            organization_id=organization.id, user_id=user.id, is_accepted=True
        )

        res = client.delete(f"{self.URL}{organization.id}/")
        assert res.status_code == status.HTTP_403_FORBIDDEN
