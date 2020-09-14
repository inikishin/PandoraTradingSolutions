from datetime import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from dailyAnalysis.models import Post
from marketDictionary.models import Ticker


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        items_list = ['mainpage', 'dailyAnalysis', 'predictions', 'contact', 'about', ]
        items_list += ['how-to-use', 'how-to-use_elder', 'how-to-use_channel', 'how-to-use_divbar',
                       'how-to-use_volatility', 'how-to-use_NR4ID', ]
        return items_list

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.created
    
class TickerSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Ticker.objects.all()

    def lastmod(self, obj):
        return datetime.now()