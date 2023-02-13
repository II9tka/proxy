#!/bin/bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do sleep 1; done;

python3 manage.py migrate
python3 manage.py createsuperuser --noinput
python3 manage.py runserver 0.0.0.0:8000

exec "$@"