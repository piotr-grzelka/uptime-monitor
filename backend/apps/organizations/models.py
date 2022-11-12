import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..contrib.utils import unique_slug

user_model = get_user_model()


class Organization(models.Model):
    """
    An organization model
    Organization has an owner and can have other users
    """

    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(_("Name"), max_length=50)
    slug = models.SlugField(_("Slug"))
    owner = models.ForeignKey(
        user_model,
        models.CASCADE,
        related_name="organizations",
        verbose_name=_("Owner"),
    )
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        unique_slug(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        ordering = ("-date_created",)


class OrganizationUser(models.Model):
    """
    Relation between organization and user with user role
    admin role - can manage users, checkpoints, integrations, etc...
    user role - only can view stats and receive notifications
    only organization owner can transfer ownership of organization
    """

    ROLE_ADMIN = "admin"
    ROLE_USER = "user"

    ROLES = (
        (ROLE_ADMIN, _("Admin")),
        (ROLE_USER, _("User")),
    )

    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    organization = models.ForeignKey(
        Organization,
        models.CASCADE,
        related_name="users",
        verbose_name=_("Organization"),
    )
    user = models.ForeignKey(user_model, models.CASCADE, verbose_name=_("User"))
    role = models.CharField(_("Role"), max_length=5, choices=ROLES, default=ROLE_USER)
    is_accepted = models.BooleanField(_("Is accepted"), default=False)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True)
    date_accepted = models.DateTimeField(_("Date accepted"), null=True, blank=True)

    def __str__(self):
        return (
            f"{self.organization.name} - {self.user.first_name} {self.user.last_name}"
        )

    class Meta:
        verbose_name = _("Organization user")
        verbose_name_plural = _("Organization users")
        ordering = ("-date_created",)
