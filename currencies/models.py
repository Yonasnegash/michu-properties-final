from django.db import models
from datetime import datetime

class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Currencie"