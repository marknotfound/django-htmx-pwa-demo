const site = "django-htmx-pwa-demo-v1"
const assets = [
  "/",
  "/feed/",
  "/profile/",
  "/static/images/icons/100.png",
  "/static/images/icons/1024.png",
  "/static/images/icons/114.png",
  "/static/images/icons/120.png",
  "/static/images/icons/128.png",
  "/static/images/icons/144.png",
  "/static/images/icons/152.png",
  "/static/images/icons/16.png",
  "/static/images/icons/167.png",
  "/static/images/icons/180.png",
  "/static/images/icons/192.png",
  "/static/images/icons/20.png",
  "/static/images/icons/256.png",
  "/static/images/icons/29.png",
  "/static/images/icons/32.png",
  "/static/images/icons/40.png",
  "/static/images/icons/50.png",
  "/static/images/icons/512.png",
  "/static/images/icons/57.png",
  "/static/images/icons/58.png",
  "/static/images/icons/60.png",
  "/static/images/icons/64.png",
  "/static/images/icons/72.png",
  "/static/images/icons/76.png",
  "/static/images/icons/80.png",
  "/static/images/icons/87.png",
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