from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class SmsApiPlChannel(BaseChannel):
    """
    Sends SMS notifications via smsapi.pl
    """

    title = _("SMS")

    def form_fields(self):
        return [
            {"kind": "char", "name": "phone", "label": "Phone number", "validators": []}
        ]


class TwilioChannel(BaseChannel):
    """
    Sends SMS notifications via Twilio
    """

    title = _("SMS")

    def form_fields(self):
        return [
            {"kind": "char", "name": "phone", "label": "Phone number", "validators": []}
        ]
