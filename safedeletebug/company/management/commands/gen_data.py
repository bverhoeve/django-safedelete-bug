from company import factories
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for _ in range(20):
            company = factories.CompanyFactory()
            company.save()
