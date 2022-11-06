from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from rest_framework.schemas import get_schema_view

admin.site.site_header = ""
admin.site.site_title = ""
admin.site.index_title = ""

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/docs/",
        include_docs_urls(
            title="Rest API",
            permission_classes=[
                AllowAny,  # type: ignore
            ],
        ),
    ),
    path(
        "api/v1/schema/",
        get_schema_view(
            title="Uptime Monitor REST API",
            description="",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path("api/v1/accounts/", include("apps.accounts.urls")),
    path("api/v1/organizations/", include("apps.organizations.urls")),
    path("api/v1/services/", include("apps.services.urls")),
    path("api/v1/notify/", include("apps.notify.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
