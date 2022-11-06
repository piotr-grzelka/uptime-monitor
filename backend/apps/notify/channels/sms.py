from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class SmsApiPlChannel(BaseChannel):
    title = _("SMS")

    def form_fields(self):
        return [
            {"kind": "char", "name": "phone", "label": "Phone number", "validators": []}
        ]


class TwilioChannel(BaseChannel):
    title = _("SMS")

    def form_fields(self):
        return [
            {"kind": "char", "name": "phone", "label": "Phone number", "validators": []}
        ]
