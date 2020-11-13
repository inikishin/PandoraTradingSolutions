from django.db import models

class Market(models.Model):
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=300)
    site = models.CharField(max_length=300)

    def __str__(self):
        return self.short_name

class Ticker(models.Model):
    short_name = models.CharField(max_length=20)
    ticker_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=300)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    site = models.CharField(max_length=300)
    seo_content = models.TextField()

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return "/marketdictionary/{0}/".format(self.short_name)
