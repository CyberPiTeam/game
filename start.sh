#!/usr/bin/env sh
python manage.py migrate
#set the port for the server to run on and address
gunicorn --workers=4 --bind=0.0.0.0:8000 cyberpi_dress_up_game.wsgi:application
