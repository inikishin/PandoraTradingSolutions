from django.db import models
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse

from django.dispatch import receiver
from django.db.models.signals import post_save

class Article(FlatPage):
    custom_fLate_page = models.OneToOneField(FlatPage, on_delete=models.CASCADE, parent_link=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)
    date_pub = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='admin')

    def get_absolute_url(self):
    	return reverse('article:blog_post', args=[self.slug])

    @receiver(post_save, sender=User) 
    def create_or_update_user_profile(sender, instance, created, **kwargs):
    	if created:
    		Profile.objects.create(user=instance) 
    		instance.profile.save()
