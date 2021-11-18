from django.db import models


class StatisticModel(models.Model):
    date = models.DateField()
    views = models.IntegerField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
