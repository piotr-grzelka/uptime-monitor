from django.core.management.base import BaseCommand, CommandError

from apps.accounts.models import CustomUser
from apps.accounts.tests.factories import UserFactory
from apps.organizations.tests.factories import OrganizationFactory
from apps.services.tests.factories import ServiceFactory


class Command(BaseCommand):
    help = 'Generate sample data'

    def add_arguments(self, parser):
        parser.add_argument('password', type=str)

    def handle(self, *args, **options):
        password = options['password']

        CustomUser.objects.all().delete()

        super_user = CustomUser.objects.create_superuser(
            email='test@uptime.loc',
            password=password,
            first_name='Testowy',
            last_name='Admin'
        )

        print(f"SuperUser created: {super_user.email} / {password}")

        users = UserFactory.create_batch(100)
        print(f"{len(users)} other users created")

        users.insert(0, super_user)

        organizations = [OrganizationFactory.create(owner=users[i]) for i in range(20)]
        print(f"{len(organizations)} organizations created")

        services = []
        for i in range(20):
            services += ServiceFactory.create_batch(
                size=50 - i,
                organization=organizations[i]
            )

        print(f"{len(services)} services created")
