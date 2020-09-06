from django.db import models

class Market(models.Model):
    short_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=300)
    site = models.CharField(max_length=300)

    def __str__(self):
        return self.short_name

class Ticker(models.Model):
    short_name = models.CharField(max_length=20)
    ticker_name = models.CharField(max_length=20, null=False, default=None)
    full_name = models.CharField(max_length=300)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    site = models.CharField(max_length=300)

    def __str__(self):
        return self.short_name
