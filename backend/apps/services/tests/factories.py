import factory

from ..models import Service


class ServiceFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    organization = None

    class Meta:
        model = Service
