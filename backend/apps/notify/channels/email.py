from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class EmailChannel(BaseChannel):
    title = _("Email")

    def form_fields(self):
        return [
            {
                "kind": "email",
                "name": "email",
                "label": "Email",
                "validators": [EmailValidator],
            }
        ]
