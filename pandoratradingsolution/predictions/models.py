from django.db import models
import marketDictionary.models as md

class PredictionHorizon(models.Model):
    horizon_name = models.CharField(max_length=100)
    lag = models.IntegerField(default=0)

    def __str__(self):
        return self.horizon_name

class Prediction(models.Model):
    horizon = models.ForeignKey(PredictionHorizon, on_delete=models.CASCADE)
    ticker = models.ForeignKey(md.Ticker, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    currentprice = models.FloatField(default=0)
    predictprice = models.FloatField(default=0)
    prctChange = models.FloatField(default=0)
    probability = models.FloatField(default=0)

    def getpreddate(self):
        return self.created + self.horizon.get_lag()