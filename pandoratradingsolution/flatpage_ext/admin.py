from django.contrib import admin
from .models import FlatPageExt

class FlatPageExtAdmin(admin.ModelAdmin):
    list_display = ['init_flatpage', 'date_pub', 'author']

admin.site.register(FlatPageExt, FlatPageExtAdmin)