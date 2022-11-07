import pytest
from apps.notify.channels.base import BaseChannel
from apps.notify.helpers import get_notify_channels
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.test.utils import modify_settings


def test_get_notify_channels():
    channels = get_notify_channels()
    assert len(channels) == len(settings.NOTIFY_CHANNELS)

    get_notify_channels.cache_clear()


@modify_settings(
    NOTIFY_CHANNELS={
        "append": "django.contrib.auth.hashers.Argon2PasswordHasher",
    }
)
def test_get_notify_channels_improperly_configured():
    with pytest.raises(ImproperlyConfigured):
        get_notify_channels()
    get_notify_channels.cache_clear()


def test_base_channel_form_fields_not_implemented():
    class FakeChannel(BaseChannel):
        pass

    with pytest.raises(NotImplementedError):
        FakeChannel().form_fields()
