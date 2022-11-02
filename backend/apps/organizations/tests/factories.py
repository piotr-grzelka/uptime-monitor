import factory

from ..models import Organization


class OrganizationFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("company")
    owner = None

    class Meta:
        model = Organization
