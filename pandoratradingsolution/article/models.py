from django.db import models
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
# Create your models here.

class Article(FlatPage):
    custom_fLate_page = models.OneToOneField(FlatPage, on_delete=models.CASCADE, parent_link=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    date_pub = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')
