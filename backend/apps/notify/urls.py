from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path("channels/", views.ChannelsView.as_view(), name="channels"),
    path("", include(router.urls)),
]
