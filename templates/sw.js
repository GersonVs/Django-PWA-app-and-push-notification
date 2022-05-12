var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/manifest.json',
    '/offline',
    '/static/css/styles.css',
    '/static/images/android-chrome-512x512.png',
    '/static/images/android-chrome-192x192.png',
    '/static/images/apple-touch-icon.png'
];

self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('offline');
            })
    )
});

self.addEventListener('push', function (event) {

    const eventInfo = event.data.text();
    const data = JSON.parse(eventInfo);
    const head = data.head || 'New Notification 🕺🕺';
    const body = data.body || 'This is default content. Your notification didn\'t have one 🙄🙄';

    event.waitUntil(
        self.registration.showNotification(head, {
            body: body,
            icon: 'https://i.imgur.com/MZM3K5w.png'
        })
    );
});