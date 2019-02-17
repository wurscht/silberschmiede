from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r"^website/", include("website.urls")),
    url(r"^admin/", admin.site.urls),
]
