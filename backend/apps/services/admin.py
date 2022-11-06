from django.contrib import admin

from .models import Service, ServiceNotify


class ServiceNotifyInlineAdmin(admin.TabularInline):
    """
    Inline admin for service notifications
    """

    model = ServiceNotify


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Admin view for services
    """

    list_filter = (
        "status",
        "kind",
        "is_active",
        "organization",
    )
    search_fields = ("name", "endpoint")
    list_display = ("name", "kind", "status", "kind", "is_active", "organization")
    inlines = (ServiceNotifyInlineAdmin,)
