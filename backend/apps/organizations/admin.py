from django.contrib import admin

from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    Admin view for organizations
    """

    list_filter = ("name",)
    list_display = ("name", "owner", "date_created")
