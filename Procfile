release: python manage.py build
web: gunicorn pwademo.asgi:application -k uvicorn.workers.UvicornWorker
