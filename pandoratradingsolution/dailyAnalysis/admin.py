from django.contrib import admin

from .models import AnalysisType, Post, Image

admin.site.register(AnalysisType)
admin.site.register(Post)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']


admin.site.register(Image, ImageAdmin)