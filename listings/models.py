from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

from realtors.models import Realtor
from currencies.models import Currency
from propertytypes.models import PropertyType
from virtualtours.models import VirtualTour

class Listing(models.Model):
    FEATURES = (
        ('balcony', 'balcony'),
        ('generator', 'generator'),
        ('garage', 'garage'),
        ('garden', 'garden'),
        ('water-tank', 'water-tank'),
        ('water-pump', 'water-pump'),
        ('swimming pool', 'swimming pool'),
        ('clubhouses', 'clubhouses'),
        ('tennis court', 'tennis court'),
        ('parking', 'parking'),
        ('covered parking', 'covered parking'),
        ('common areas', 'common areas'),
        ('security', 'security'),
        ('bike storage', 'bike storage'),
        ('electric car charing station', 'electric car charing station'),
        ('barbeque areas', 'barbeque areas'),
        ('picnic tables', 'picnic tables'),
        ('elevators', 'elevators'),
        ('wi-fi', 'wi-fi'),
        ('ground water', 'ground water'),
        ('basement parking', 'basement parking'),
        ('cafe & resturant', 'cafe & resturant'),
        ('gym & spa', 'gym & spa'),
        ('beauty salon', 'beauty salon'),
        ('children’s toy', 'children’s toy')
    )
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    total_rooms = models.IntegerField()
    floors = models.IntegerField(default=0)
    garage = models.IntegerField(default=0)
    parking_lot = models.IntegerField(default=0)
    property_size = models.DecimalField(max_digits=5, decimal_places=1)
    land_area = models.DecimalField(max_digits=5, decimal_places=1)
    property_type = models.ForeignKey(PropertyType, on_delete=models.DO_NOTHING)
    feature = MultiSelectField(max_length=1000, choices=FEATURES)
    year_built = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.DO_NOTHING)
    # price = models.IntegerField()
    price_per_sqm = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    discount = models.BooleanField(default=False)
    is_for_rent = models.BooleanField(default=False)
    is_furnished = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    virtual_tour = models.ForeignKey(VirtualTour, on_delete=models.CASCADE)
    floor_plan_image1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    floor_plan_image2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    floor_plan_image3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    floor_plan_image4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    floor_plan_image5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True)

    def calculate_price(self):
        prices = [round(size.size * self.price_per_sqm * self.rate, 2) for size in self.sizes.all()]
        return prices

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Propertie"

class PropertyMultiplePhoto(models.Model):
    show = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="photos"
    )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

class PropertySize(models.Model):
    listing = models.ForeignKey(Listing, related_name='sizes', on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=5, decimal_places=1)
    net_size = models.DecimalField(max_digits=5, decimal_places=1)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    def __str__(self):
        return f"{self.size} m² ({self.net_size} net) - {self.bedrooms} BR / {self.bathrooms} BA"