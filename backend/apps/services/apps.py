from django.apps import AppConfig


class ServicesConfig(AppConfig):
    """
    Services that will be monitored application
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.services"
