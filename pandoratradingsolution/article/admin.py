from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('custom_fLate_page', 'meta_description', 'meta_keywords', 'date_pub', 'author')

admin.site.register(Article, ArticleAdmin)
		