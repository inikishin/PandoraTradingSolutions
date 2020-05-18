from django.db import models
import marketDictionary.models as md
from django.conf import settings


class AnalysisType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

# markdowns for texfields
# https://pocoz.gitbooks.io/django-v-primerah/rasshirenie-prilozheniya-blog/sozdanie-kastomizirovannyh-shablonov-tegov-i-filtrov/sozdanie-filtrov-shablonizatora-django.html
# https://daringfireball.net/projects/markdown/basics


class Post(models.Model):
    analysis_type = models.ForeignKey(AnalysisType, on_delete=models.CASCADE)
    ticker = models.ForeignKey(md.Ticker, on_delete=models.CASCADE)
    date_analysis = models.DateField()
    header = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='date_analysis')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticker.short_name + '_' + str(self.date_analysis)


class Image(models.Model):
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='dailyAnalysis')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    def __str__(self):
        return self.title