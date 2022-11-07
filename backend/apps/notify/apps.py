from django.apps import AppConfig


class NotifyConfig(AppConfig):
    """
    Notify app, responsible for notification configuration and sending messages
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.notify"
