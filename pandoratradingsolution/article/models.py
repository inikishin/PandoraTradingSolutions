from django.db import models
from account.models import Profile
from django.contrib.flatpages.models import FlatPage

class Article(FlatPage):
    custom_flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE, parent_link=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    date_pub = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='admin')
