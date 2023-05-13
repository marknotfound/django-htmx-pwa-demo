from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "pwademo/base.html")


def feed(request: HttpRequest):
    response = (
        render(request, "pwademo/feed_partial.html")
        if request.headers.get("hx-request")
        else render(request, "pwademo/feed.html")
    )

    response["Vary"] = "HX-Request"
    return response


def profile(request: HttpRequest):
    response = (
        render(request, "pwademo/profile_partial.html")
        if request.headers.get("hx-request")
        else render(request, "pwademo/profile.html")
    )

    response["Vary"] = "HX-Request"
    return response


manifest = TemplateView.as_view(
    template_name="pwademo/manifest.json",
    content_type="application/json",
)

service_worker = TemplateView.as_view(
    template_name="pwademo/sw.js",
    content_type="application/javascript",
)


urlpatterns = [
    path("", index, name="index"),
    path("sw.js", service_worker, name="sw.js"),
    path("manifest.json", manifest, name="pwa-manifest"),
    path("admin/", admin.site.urls),
    path("feed/", feed, name="feed"),
    path("profile/", profile, name="profile"),
]
