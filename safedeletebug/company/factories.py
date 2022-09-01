from factory.django import DjangoModelFactory
import factory


class SectionFactory(DjangoModelFactory):
    class Meta:
        model = 'company.Section'
    
    name = factory.Faker('country')

class LocationFactory(DjangoModelFactory):
    class Meta:
        model = 'company.Location'

    class Params:
        location = factory.Faker('local_latlng')

    address = factory.Faker('address')
    latitude = factory.LazyAttribute(lambda o: float(o.location[0]))
    longitude = factory.LazyAttribute(lambda o: float(o.location[1]))
    section = factory.SubFactory(SectionFactory)

class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = 'company.Company'
    
    name = factory.Faker('company')
    billing_location = factory.SubFactory(LocationFactory)
    section = factory.LazyAttribute(lambda obj: obj.billing_location.section)


