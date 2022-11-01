from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path(
        "register-confirm/",
        views.RegisterConfirmView.as_view(),
        name="register_confirm",
    ),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),
    path("", include(router.urls)),
]
