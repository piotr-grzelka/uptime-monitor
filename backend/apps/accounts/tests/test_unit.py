import pytest
from apps.accounts.models import CustomUser


def test_user_manager_create_user_without_email():
    with pytest.raises(ValueError):
        CustomUser.objects.create_user(None)


@pytest.mark.django_db
def test_user_manager_create_user_ok():
    CustomUser.objects.create_user("test@test.pl", "t1t1")

    model: CustomUser = CustomUser.objects.filter(email="test@test.pl").get()
    assert model.is_staff is False
    assert model.is_superuser is False
    assert str(model.password).startswith("argon")


@pytest.mark.django_db
def test_user_manager_create_superuser_ok():
    CustomUser.objects.create_superuser("test1@test.pl", "t1t1")

    model: CustomUser = CustomUser.objects.filter(email="test1@test.pl").get()
    assert model.is_staff is True
    assert model.is_superuser is True


def test_user_unicode_representation():
    model: CustomUser = CustomUser(first_name="john", last_name="do")
    assert model.get_full_name() == "john do"
    assert str(model) == "john do"
