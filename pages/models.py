from django.db import models

from datetime import datetime

class Subscriber(models.Model):
    email = models.CharField(max_length=100)
    subsribed_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.email
