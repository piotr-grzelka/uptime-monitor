from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class PushoverChannel(BaseChannel):
    title = _("Pushover")

    def form_fields(self):
        return [
            {"kind": "char", "name": "token", "label": "Token", "validators": []},
            {"kind": "char", "name": "user", "label": "User", "validators": []},
        ]
