from django.core.management import BaseCommand
from home_work_lesson2.models import Client

class Command(BaseCommand):
    help = "create client"

    def handle(self, *args, **options):
        client = Client(
            name="Nikolay",
            email="adasd@adsasd.ru",
            number="12313123",
            addres="asdasdasdasd",
            registr_date='2009-12-01',
        )
        client.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created client: {client.name}'))
