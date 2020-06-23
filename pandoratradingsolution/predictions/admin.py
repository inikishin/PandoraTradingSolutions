from django.contrib import admin
from .models import PredictionHorizon, Prediction

admin.site.register(PredictionHorizon)

class PredictionAdmin(admin.ModelAdmin):
    list_display = ['ticker', 'horizon', 'created', 'currentprice', 'predictprice', 'prctChange', 'probability']
    list_filter = ['created', 'ticker', 'horizon']

admin.site.register(Prediction, PredictionAdmin)