from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class FormFieldSerializer(serializers.Serializer):
    """
    Notify channel form field serializer
    """

    kind = serializers.CharField(label=_("Kind"))
    name = serializers.CharField(label=_("Name"))
    title = serializers.CharField(label=_("Title"))

    def update(self, *args, **kwargs):
        """temporary unavailable"""

    def create(self, *args, **kwargs):
        """temporary unavailable"""

    class Meta:
        fields = ("kind", "name", "title")


class NotifyChannelSerializer(serializers.Serializer):
    """
    Notify channel serializer
    """

    kind = serializers.CharField(label=_("Kind"))
    title = serializers.CharField(label=_("Title"))
    form_fields = FormFieldSerializer(many=True)

    def update(self, *args, **kwargs):
        """temporary unavailable"""

    def create(self, *args, **kwargs):
        """temporary unavailable"""

    class Meta:
        fields = (
            "kind",
            "title",
            "form_fields",
        )
