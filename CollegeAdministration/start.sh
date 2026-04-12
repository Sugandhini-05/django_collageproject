#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn CollegeAdministration.wsgi:application --bind 0.0.0.0:$PORT