from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("nikolai/", include('nikolai.urls')),
    path('admin/', admin.site.urls)
]
