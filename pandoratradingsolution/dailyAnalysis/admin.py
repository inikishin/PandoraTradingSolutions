from django.contrib import admin
from .models import AnalysisType, Post

admin.site.register(AnalysisType)


class PostAdmin(admin.ModelAdmin):
    list_display = ['header', 'slug', 'ticker', 'created']
    list_filter = ['created', 'ticker']


admin.site.register(Post, PostAdmin)