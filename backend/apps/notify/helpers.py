import functools

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string

from .channels.base import BaseChannel


@functools.lru_cache
def get_notify_channels():
    """
    returns all available notify channels
    @return:
    """
    channels = []
    for ch_path in settings.NOTIFY_CHANNELS:
        ch_cls = import_string(ch_path)
        channel = ch_cls()
        if not isinstance(channel, BaseChannel):
            raise ImproperlyConfigured(
                f"channel doesn't inherit from BaseChannel: {ch_path}"
            )
        channels.append(channel)
    return channels


# @functools.lru_cache
# def get_notify_channels_for_choice_field():
#     return list(
#         (channel.kind(), "channel.label()") for channel in get_notify_channels()
#     )
