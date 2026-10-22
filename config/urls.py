"""URL configuration. See https://docs.djangoproject.com/en/6.1/topics/http/urls/"""

from django.contrib import admin
from django.urls import path

from notes import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
]
