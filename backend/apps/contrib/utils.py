from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


def unique_slug(
    instance: models.Model, value_field_name="name", slug_field_name="slug"
):
    """
    Generate an unique slug for given value

    @param instance:
    @param value_field_name:
    @param slug_field_name:
    @return:
    """
    value_field = instance._meta.get_field(value_field_name)
    slug_field = instance._meta.get_field(slug_field_name)

    value = getattr(instance, value_field.attname)  # type: ignore
    max_length: int = slug_field.max_length  # type: ignore

    slug = slugify(value)[:max_length]

    queryset = (
        instance.__class__._default_manager.all()  # pylint: disable=protected-access
    )
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    while queryset.filter(**{slug_field_name: slug}).exists():
        slug = slug[: max_length - 4] + get_random_string(4)

    setattr(instance, slug_field.attname, slug)  # type: ignore
