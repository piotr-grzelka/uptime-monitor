from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class SmsApiPlChannel(BaseChannel):
    label = _("SMS")


class TwilioChannel(BaseChannel):
    label = _("SMS")
