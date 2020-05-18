from django.contrib import admin

from .models import Ticker, Market

admin.site.register(Ticker)
admin.site.register(Market)