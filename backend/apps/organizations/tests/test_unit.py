from ...accounts.models import CustomUser
from ..models import Organization, OrganizationUser


def test_organization_unicode():
    model = Organization(name="testowa")
    assert str(model) == "testowa"


def test_organization_user_unicode():
    user = CustomUser(first_name="john", last_name="do")
    organization = Organization(name="testowa")
    model = OrganizationUser(user=user, organization=organization)
    assert str(model) == "testowa - john do"
