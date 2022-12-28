from django.db import models

class VirtualTour(models.Model):
    title = models.CharField(max_length=1024)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Virtual Tour"

class VirtualTourPhotos(models.Model):
    show = models.ForeignKey(
        VirtualTour, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
