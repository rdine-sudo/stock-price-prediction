from django.db import models

# Create your models here.



class CoinData(models.Model):
    Date            = models.DateTimeField(max_length=255,default='', null=True, blank=True)
    Open            = models.FloatField(default=None)
    High            = models.FloatField(default=None)
    Low             = models.FloatField(default=None)
    Close           = models.FloatField(default=None)
    AdjClose        = models.FloatField(default=None)
    Volume          = models.FloatField(default=None)
    name            = models.CharField(max_length=255, default=None)



class ForecastedTrend(models.Model):
    Date            = models.DateTimeField(max_length=255,default='', null=True, blank=True)
    Forecast        = models.FloatField(default=None)
    name            = models.CharField(max_length=255, default=None)



class Currency(models.Model):
    name            = models.CharField(max_length=255, default=None)
    symbol            = models.CharField(max_length=255, default=None)

