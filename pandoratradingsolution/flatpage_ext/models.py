from django.db import models
from django.contrib.flatpages.models import FlatPage

from account.models import Profile

class FlatPageExt(models.Model):
    init_flatpage = models.OneToOneField(FlatPage, on_delete=models.CASCADE)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    date_pub = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='admin')