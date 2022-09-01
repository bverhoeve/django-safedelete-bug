from django.http import HttpResponse
from .models import Location

def index(request):

    locations = Location.objects.filter(
        latitude__gte=0.0, 
        latitude__lte=50, 
        longitude__gte=1.0, 
        longitude__lte=40,
    ).exclude(billing_location_for_company__isnull=False).all()

    location_ids = [loc.pk for loc in locations]


    return HttpResponse(f'Locations {location_ids}')
