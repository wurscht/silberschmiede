from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r"^", include("website.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^", include("cms.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
