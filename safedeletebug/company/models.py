from django.db import models
from safedelete.models import SafeDeleteModel

class Section(SafeDeleteModel):
    name = models.CharField(verbose_name='name', blank=True, max_length=255)

class Location(SafeDeleteModel):
    address = models.CharField(verbose_name='Address', blank=True, max_length=255)
    latitude = models.FloatField(verbose_name='Latitude', default=0.0)
    longitude = models.FloatField(verbose_name='Longitude', default=0.0)
    section = models.ForeignKey(to=Section, verbose_name='Section', on_delete=models.CASCADE)

class Company(SafeDeleteModel):
    name = models.CharField(verbose_name='Name', blank=True, max_length=255)
    billing_location = models.ForeignKey(to=Location, verbose_name='Billing location', null=True, on_delete=models.PROTECT, related_name='billing_location_for_company')
    section = models.ForeignKey(to=Section, verbose_name='Section', on_delete=models.CASCADE)
