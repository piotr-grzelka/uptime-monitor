from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class PushoverChannel(BaseChannel):
    """
    Sends notifications via pushover
    """

    title = _("Pushover")

    def form_fields(self):
        return [
            {"kind": "char", "name": "token", "title": "Token", "validators": []},
            {"kind": "char", "name": "user", "title": "User", "validators": []},
        ]
