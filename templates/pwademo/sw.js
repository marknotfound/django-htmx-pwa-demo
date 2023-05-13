const site = "django-htmx-pwa-demo-v1"
const assets = [
  "/",
  "/feed/",
  "/profile/",
];

self.addEventListener("install", installEvent => {
  installEvent.waitUntil(
    caches.open(site).then(cache => {
      cache.addAll(assets)
    })
  )
});

self.addEventListener("fetch", fetchEvent => {
  fetchEvent.respondWith(
    caches.match(fetchEvent.request).then(res => {
      return res || fetch(fetchEvent.request)
    })
  )
});
