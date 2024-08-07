from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, bathroom_choices, house_type, city_choices, sqft_choices

from listings.models import Listing

# Coming soon scripts
from pages.models import Subscriber
from django.contrib import messages

def index(request):
    # listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    # featured_listing = Listing.objects.all().filter(is_featured=True)
    # photos = Listing.objects.all

    # context = {
    #     'listings': listings,
    #     'price_choices': price_choices,
    #     'bedroom_choices': bedroom_choices,
    #     'bathroom_choices': bathroom_choices,
    #     'house_type': house_type,
    #     'city_choices': city_choices,
    #     'sqft_choices': sqft_choices,
    #     'featured_listing': featured_listing,
    #     'photos': photos
    # }

    # return render(request, 'pages/index.html', context)
    if request.method == 'POST':
        email = request.POST['email']

        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You have already subscribed. Thank you!')
            return redirect('index')
        else:
            subscribtion = Subscriber.objects.create(email=email)
            subscribtion.save()
            messages.success(request, 'You have subscribed successfuly, you\'ll be notified when we launch. Thank you!')
            return redirect('index')
    else:
        return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contactus(request):
    return render(request, 'pages/contactus.html')

def comingsoon(request):
    return render(request, 'pages/coming_soon.html')

def travelagency(request):
    return render(request, 'pages/travel_agency.html')
