from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, bathroom_choices, house_type, city_choices, sqft_choices

from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    featured_listing = Listing.objects.all().filter(is_featured=True)
    photos = Listing.objects.all

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'house_type': house_type,
        'city_choices': city_choices,
        'sqft_choices': sqft_choices,
        'featured_listing': featured_listing,
        'photos': photos
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contactus(request):
    return render(request, 'pages/contactus.html')
