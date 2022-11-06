import psycopg2
import pytest
from apps.accounts.models import CustomUser
from apps.accounts.tests.factories import UserFactory
from apps.organizations.models import Organization
from apps.organizations.tests.factories import OrganizationFactory
from django.db import connections
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


@pytest.fixture
def user(db) -> CustomUser:
    return UserFactory.create()


@pytest.fixture
def organization(db) -> Organization:
    return OrganizationFactory.create(owner=UserFactory.create())


def run_sql(sql, dbname="postgres"):
    from django.conf import settings

    conn = psycopg2.connect(
        dbname=dbname,
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        host=settings.DATABASES["default"]["HOST"],
        port=settings.DATABASES["default"]["PORT"],
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


@pytest.fixture(scope="session")
def django_db_setup():
    from django.conf import settings

    app_database_name = settings.DATABASES["default"]["NAME"]
    test_database_name = app_database_name + "_test"

    settings.DATABASES["default"]["NAME"] = test_database_name

    run_sql(f"DROP DATABASE IF EXISTS {test_database_name}")
    run_sql(f"CREATE DATABASE {test_database_name} TEMPLATE {app_database_name}")

    yield

    for connection in connections.all():
        connection.close()

    run_sql(f"DROP DATABASE {test_database_name}")
