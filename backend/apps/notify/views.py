from apps.notify.helpers import get_notify_channels
from apps.notify.serializers import NotifyChannelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ChannelsView(APIView):
    serializer_class = NotifyChannelSerializer

    def get(self, request):
        serializer = self.serializer_class()
        items = [
            serializer.to_representation(instance=channel)
            for channel in get_notify_channels()
        ]

        return Response(data=items)
