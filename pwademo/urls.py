from django.http.request import HttpRequest
from django.contrib import admin
from django.urls import path, re_path, reverse
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "pwademo/base.html")


def feed(request: HttpRequest):
    if request.headers.get("hx-request"):
        return render(request, "pwademo/feed_partial.html")

    return render(request, "pwademo/feed.html")


def profile(request: HttpRequest):
    if request.headers.get("hx-request"):
        return render(request, "pwademo/profile_partial.html")

    return render(request, "pwademo/profile.html")


urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("feed/", feed, name="feed"),
    path("profile/", profile, name="profile"),
]
