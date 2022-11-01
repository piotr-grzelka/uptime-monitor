import pytest
from django.core import mail

from ..helpers import generate_token_for_user
from ..models import CustomUser


@pytest.mark.django_db
class TestAccountRegister:
    def test_get_not_allowed(self, client):
        response = client.get("/api/v1/accounts/register/")
        assert response.status_code == 405

    def test_validation_empty_data(self, client):
        response = client.post("/api/v1/accounts/register/", data={})
        assert response.data.keys().__len__() == 5
        assert "first_name" in response.data
        assert "last_name" in response.data
        assert "email" in response.data
        assert "password" in response.data
        assert response.status_code == 400

    def test_validation_invalid_email(self, client):
        response = client.post(
            "/api/v1/accounts/register/",
            data={
                "first_name": "valid",
                "last_name": "valid",
                "email": "invalid",
                "password": "validPassword123",
                "password_repeat": "validPassword123",
            },
        )
        assert response.data.keys().__len__() == 1
        assert "email" in response.data
        assert response.status_code == 400

    def test_validation_invalid_password(self, client):
        response = client.post(
            "/api/v1/accounts/register/",
            data={
                "first_name": "valid",
                "last_name": "valid",
                "email": "valid@example.com",
                "password": "v",
                "password_repeat": "validPassword123",
            },
        )
        assert response.data.keys().__len__() == 2
        assert "password" in response.data
        assert "password_repeat" in response.data
        assert response.status_code == 400

    def test_valid_registration(self, client):
        response = client.post(
            "/api/v1/accounts/register/",
            data={
                "first_name": "valid",
                "last_name": "valid",
                "email": "valid@example.com",
                "password": "validPassword123",
                "password_repeat": "validPassword123",
            },
        )
        assert response.status_code == 201
        user_from_db: CustomUser = CustomUser.objects.filter(
            email="valid@example.com"
        ).get()
        assert user_from_db is not None
        assert user_from_db.password != "validPassword123"

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == "Activate your user account."


@pytest.mark.django_db
class TestAccountRegisterConfirmation:
    def test_get_not_allowed(self, client):
        response = client.get("/api/v1/accounts/register-confirm/")
        assert response.status_code == 405

    def test_validation_empty_data(self, client):
        response = client.post("/api/v1/accounts/register-confirm/", data={})
        assert response.data.keys().__len__() == 1
        assert "token" in response.data
        assert response.status_code == 400

    def test_invalid_token(self, client):
        response = client.post("/api/v1/accounts/register-confirm/", data={
            "token": "invalid token"
        })
        assert response.data.keys().__len__() == 1
        assert response.status_code == 400
        assert "token" in response.data
        assert response.data['token'] == 'Provided token is malformed.'

    def test_token_expired(self, client, user: CustomUser):
        token = generate_token_for_user(user, 0)

        response = client.post("/api/v1/accounts/register-confirm/", data={
            "token": token
        })

        assert response.data.keys().__len__() == 1
        assert response.status_code == 400
        assert "token" in response.data
        assert response.data['token'] == 'Provided token is expired.'

    def test_user_not_found(self, client, user: CustomUser):
        token = generate_token_for_user(user, 1)
        user.delete()

        response = client.post("/api/v1/accounts/register-confirm/", data={
            "token": token
        })

        assert response.data.keys().__len__() == 1
        assert response.status_code == 404

    def test_user_already_confirmed(self, client, user: CustomUser):
        user.is_verified = True
        user.save()

        token = generate_token_for_user(user, 1)

        response = client.post("/api/v1/accounts/register-confirm/", data={
            "token": token
        })

        assert response.data.keys().__len__() == 1
        assert response.status_code == 400
        assert "token" in response.data
        assert response.data['token'] == 'User already confirmed.'

    def test_valid_confirmation(self, client, user: CustomUser):
        token = generate_token_for_user(user, 1)

        response = client.post("/api/v1/accounts/register-confirm/", data={
            "token": token
        })

        assert response.data.keys().__len__() == 1
        assert response.status_code == 204
        user.refresh_from_db()
        assert user.is_verified
