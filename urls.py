from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
    path("", include("myapp1.urls")),
    path("", include("myapp2.urls")),
]