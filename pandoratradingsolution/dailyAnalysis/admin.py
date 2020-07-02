from django.contrib import admin
from .models import AnalysisType, Post

admin.site.register(AnalysisType)


class PostAdmin(admin.ModelAdmin):
    list_display = ['header', 'slug', 'ticker', 'created', 'sig_elder', 'sig_channel', 'sig_DivBar', 'sig_NR4ID', 'sig_breakVolatility']
    list_filter = ['created', 'ticker']
    search_fields = ['header']

admin.site.register(Post, PostAdmin)