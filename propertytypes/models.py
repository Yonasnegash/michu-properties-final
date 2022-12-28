from django.db import models
from datetime import datetime

class PropertyType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Property Type"
