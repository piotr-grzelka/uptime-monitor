from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers import get_notify_channels
from .serializers import NotifyChannelSerializer


class ChannelsView(APIView):
    """
    Returns all available channels
    """

    serializer_class = NotifyChannelSerializer

    def get(self, request):
        """list view"""
        serializer = self.serializer_class()
        items = [
            serializer.to_representation(instance=channel)
            for channel in get_notify_channels()
        ]

        return Response(data=items)
