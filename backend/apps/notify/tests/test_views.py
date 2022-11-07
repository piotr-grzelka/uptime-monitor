import pytest
from django.test.client import Client
from rest_framework import status

from ...accounts.models import CustomUser


@pytest.mark.django_db
class TestNotifyChannelsViewSet:
    URL = "/api/v1/notify/channels/"

    def test_unauthorized(self, client: Client):
        res = client.get(self.URL)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_list(self, client: Client, user: CustomUser):
        client.force_login(user)
        res = client.get(self.URL)
        assert res.status_code == status.HTTP_200_OK
        data = res.json()
        assert data.__len__() == 3
