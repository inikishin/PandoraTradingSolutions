import os

from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect

from .models import AnalysisType, Post

admin.site.register(AnalysisType)


class PostAdmin(admin.ModelAdmin):
    list_display = ['header', 'slug', 'slug_url', 'ticker', 'created', 'sig_elder', 'sig_channel', 'sig_DivBar', 'sig_NR4ID', 'sig_breakVolatility']
    list_filter = ['created', 'ticker']
    search_fields = ['header']

    change_list_template = "admin/model_change_list.html"

    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        custom_urls = [
            path('garbage_collector/', self.process_garbage, name='process_garbage')]
        return custom_urls + urls

    def process_garbage(self, request):
        posts = Post.objects.all()
        uuid_list = []
        for p in posts:
            uuid_list.append(p.slug)

        cd = os.path.abspath(os.curdir)
        media_path = os.path.split(cd)[0] + r'/pandoratradingsolution/media/dailyAnalysis'

        del_files = 0
        count_before = len(os.listdir(media_path))
        for i in os.listdir(media_path):
            file_uuid = i.split('_')[-1].split('.')[0]
            if file_uuid not in uuid_list:
                del_files += 1
                os.remove(media_path + r'/' + i)

        self.message_user(request, f"Всего в каталоге было { count_before } файлов. Из них было удалено  { del_files } файлов")
        return HttpResponseRedirect("../")

admin.site.register(Post, PostAdmin)