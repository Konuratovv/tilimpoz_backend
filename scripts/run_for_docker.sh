#!/usr/bin/env bash
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py shell < scripts/create-superuser.py
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3