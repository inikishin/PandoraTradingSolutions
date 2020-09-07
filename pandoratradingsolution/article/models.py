from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
# Create your models here.

class Article(FlatPage):
    custom_fLate_page = models.OneToOneField(FlatPage, on_delete=models.CASCADE, parent_link=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    date_pub = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='admin')

    def get_absolute_url(self):
    	return reverse('article:blog_post', args=[self.slug])
