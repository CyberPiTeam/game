#!/usr/bin/env bash
python manage.py migrate
#set the port for the server to run on and address
python manage.py runserver 0.0.0.0:8000