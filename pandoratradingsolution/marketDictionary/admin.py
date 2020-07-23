from django.contrib import admin

from .models import Ticker, Market

admin.site.register(Market)

class TickerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'ticker_name', 'full_name', 'market', 'site']
    list_filter = ['market', 'short_name']
    search_fields = ['ticker_name']

admin.site.register(Ticker, TickerAdmin)

