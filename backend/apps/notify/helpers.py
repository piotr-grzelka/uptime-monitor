import functools

from apps.notify.channels.base import BaseChannel
from config import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string


# @functools.lru_cache
def get_notify_channels():
    channels = []
    for ch_path in settings.NOTIFY_CHANNELS:
        ch_cls = import_string(ch_path)
        channel = ch_cls()
        if not isinstance(channel, BaseChannel):
            raise ImproperlyConfigured(
                "channel doesn't inherit from BaseChannel: %s" % ch_path
            )
        channels.append(channel)
    return channels


# @functools.lru_cache
# def get_notify_channels_for_choice_field():
#     return list(
#         (channel.kind(), "channel.label()") for channel in get_notify_channels()
#     )
