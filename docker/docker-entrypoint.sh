#!/bin/bash
service nginx start
gunicorn bankruptcy-docker.wsgi:application --bind 0.0.0.0:8000 --timeout 3600
exec "$@"