from django.http.request import HttpRequest
from django.http.response import JsonResponse
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


def manifest(request: HttpRequest):
    manifest = {
        "name": "Django/HTMX PWA Demo",
        "short_name": "DjangoHTMXPWA",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#fdfdfd",
        "theme_color": "#db4938",
        "orientation": "portrait-primary",
        "icons": [
            {
                "src": "/static/images/icons/100.png",
                "type": "image/png",
                "sizes": "100x100",
            },
            {
                "src": "/static/images/icons/1024.png",
                "type": "image/png",
                "sizes": "1024x1024",
            },
            {
                "src": "/static/images/icons/114.png",
                "type": "image/png",
                "sizes": "114x114",
            },
            {
                "src": "/static/images/icons/120.png",
                "type": "image/png",
                "sizes": "120x120",
            },
            {
                "src": "/static/images/icons/128.png",
                "type": "image/png",
                "sizes": "128x128",
            },
            {
                "src": "/static/images/icons/144.png",
                "type": "image/png",
                "sizes": "144x144",
            },
            {
                "src": "/static/images/icons/152.png",
                "type": "image/png",
                "sizes": "152x152",
            },
            {
                "src": "/static/images/icons/16.png",
                "type": "image/png",
                "sizes": "16x16",
            },
            {
                "src": "/static/images/icons/167.png",
                "type": "image/png",
                "sizes": "167x167",
            },
            {
                "src": "/static/images/icons/180.png",
                "type": "image/png",
                "sizes": "180x180",
            },
            {
                "src": "/static/images/icons/192.png",
                "type": "image/png",
                "sizes": "192x192",
            },
            {
                "src": "/static/images/icons/20.png",
                "type": "image/png",
                "sizes": "20x20",
            },
            {
                "src": "/static/images/icons/256.png",
                "type": "image/png",
                "sizes": "256x256",
            },
            {
                "src": "/static/images/icons/29.png",
                "type": "image/png",
                "sizes": "29x29",
            },
            {
                "src": "/static/images/icons/32.png",
                "type": "image/png",
                "sizes": "32x32",
            },
            {
                "src": "/static/images/icons/40.png",
                "type": "image/png",
                "sizes": "40x40",
            },
            {
                "src": "/static/images/icons/50.png",
                "type": "image/png",
                "sizes": "50x50",
            },
            {
                "src": "/static/images/icons/512.png",
                "type": "image/png",
                "sizes": "512x512",
            },
            {
                "src": "/static/images/icons/57.png",
                "type": "image/png",
                "sizes": "57x57",
            },
            {
                "src": "/static/images/icons/58.png",
                "type": "image/png",
                "sizes": "58x58",
            },
            {
                "src": "/static/images/icons/60.png",
                "type": "image/png",
                "sizes": "60x60",
            },
            {
                "src": "/static/images/icons/64.png",
                "type": "image/png",
                "sizes": "64x64",
            },
            {
                "src": "/static/images/icons/72.png",
                "type": "image/png",
                "sizes": "72x72",
            },
            {
                "src": "/static/images/icons/76.png",
                "type": "image/png",
                "sizes": "76x76",
            },
            {
                "src": "/static/images/icons/80.png",
                "type": "image/png",
                "sizes": "80x80",
            },
            {
                "src": "/static/images/icons/87.png",
                "type": "image/png",
                "sizes": "87x87",
            },
        ],
    }
    return JsonResponse(manifest)


urlpatterns = [
    path("", index, name="index"),
    path("manifest.json", manifest, name="pwa-manifest"),
    path("admin/", admin.site.urls),
    path("feed/", feed, name="feed"),
    path("profile/", profile, name="profile"),
]
