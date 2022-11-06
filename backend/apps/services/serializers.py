from rest_framework import serializers

from .models import Service, ServiceNotify


class ServiceNotifySerializer(serializers.ModelSerializer):
    """
    Serializer for service notify
    """

    class Meta:
        model = ServiceNotify
        fields = ("id", "delay", "message", "channel", "configuration")


class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer for service instance
    """

    notifications = ServiceNotifySerializer(many=True, required=False)

    class Meta:
        model = Service
        fields = (
            "id",
            "name",
            "status",
            "is_active",
            "kind",
            "endpoint",
            "port",
            "date_created",
            "date_updated",
            "check_interval",
            "availability",
            "notifications",
        )
