from django.contrib import admin

from .models import Player

# game database becomes visible on django's admin portal
admin.site.register(Player)
