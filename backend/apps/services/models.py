import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.services.notify import CHANNELS


class Service(models.Model):
    """
    Service instance that will be checked with specified interval.
    """

    STATUS_CHECKING = 'checking'
    STATUS_UP = 'up'
    STATUS_DOWN = 'down'
    STATUS_FAIL = 'down'
    STATUS_PAUSED = 'paused'

    STATUSES = (
        (STATUS_CHECKING, _("Checking")),
        (STATUS_UP, _("UP")),
        (STATUS_DOWN, _("DOWN")),
        (STATUS_FAIL, _("FAIL")),
        (STATUS_PAUSED, _("PAUSED")),
    )

    KIND_WEBSITE = 'website'
    KIND_WS = 'ws'
    KIND_ICMP_PING = 'icmp-ping'
    KIND_INCOMING = 'incoming'

    KINDS = (
        (KIND_WEBSITE, _("Website")),
        (KIND_WS, _("WebSocket")),
        (KIND_ICMP_PING, _("ICMP-PING")),
        (KIND_INCOMING, _("Incoming request")),
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(_("Friendly name"), max_length=100)
    status = models.CharField(_("Status"), max_length=10, choices=STATUSES, default=STATUS_CHECKING)

    is_active = models.BooleanField(_("Is active"), default=False)

    kind = models.CharField(_("Kind"), max_length=10, choices=KINDS)

    endpoint = models.CharField(_("Endpoint"), max_length=200, null=True, blank=True)
    port = models.PositiveIntegerField(_("Port"), null=True, blank=True)

    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True)

    check_interval = models.DurationField(_("Check interval"), default='PT1M')

    last_checked = models.DateTimeField(_("Last checked"), null=True, blank=True)

    availability = models.PositiveIntegerField(_("Percentage availability"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ('-date_created',)


class ServiceNotify(models.Model):
    """
    Notify configuration
    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    service = models.ForeignKey(Service, models.CASCADE, verbose_name=_("Service"))

    delay = models.PositiveIntegerField(_("Notify delay"), default=0)
    message = models.CharField(_("Additional message"), max_length=200, null=True, blank=True)

    channel = models.CharField(_("Channel"), max_length=100, choices=CHANNELS)

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ('id',)
