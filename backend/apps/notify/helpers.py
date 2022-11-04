import functools

from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string

from config import settings


@functools.lru_cache
def get_notify_channels():
    channels = []
    for ch_path in settings.NOTIFY_CHANNELS:
        ch_cls = import_string(ch_path)
        channel = ch_cls()
        if not getattr(channel, "label"):
            raise ImproperlyConfigured(
                "channel doesn't specify an label: %s" % ch_path
            )
        channels.append(channel)
    return channels
