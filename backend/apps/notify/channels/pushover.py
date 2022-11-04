from django.utils.translation import gettext_lazy as _

from .base import BaseChannel


class PushoverChannel(BaseChannel):
    label = _("Pushover")
