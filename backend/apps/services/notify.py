from django.utils.translation import gettext_lazy as _


class BaseNotify:
    label = None


class EmailNotify(BaseNotify):
    label = _("Email")


class PushoverNotify(BaseNotify):
    label = _("Pushover")


class SMSNotify(BaseNotify):
    label = _("SMS")


CHANNELS = list(
    (cl().__class__.__module__, cl().label) for cl in BaseNotify.__subclasses__()
)

print(CHANNELS)
