from django.contrib import admin
from django.urls import path, include

app_name = "user"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("authentication", include("authentication.urls")),
]
