# Django/HTMX/PWA Demo
This is an app demoing one way to build a PWA using Django. It uses
* [Workbox](https://developer.chrome.com/docs/workbox/) for the service worker
* [HTMX](https://github.com/bigskysoftware/htmx) for SPA-like navigation
* [Hyperscript](https://github.com/bigskysoftware/_hyperscript) for interactivity (ok, really just toggling navbar classes)

## Run Locally
```
pipenv install
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run dev
open http://127.0.0.1:8000/
```

## Demo App
This is hosted online on [Railway](https://railway.app). You can view (and install!) the demo app here: [https://django-htmx-pwa-demo-production.up.railway.app/](https://django-htmx-pwa-demo-production.up.railway.app/)

Visiting the above link on an Android phone will prompt you to install the app. Visiting on iOS, you will need to navigate to `Share -> Add to Home Screen` to install the app.