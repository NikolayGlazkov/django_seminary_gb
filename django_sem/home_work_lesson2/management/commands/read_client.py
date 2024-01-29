from django.core.management import BaseCommand
from home_work_lesson2.models import Client


class Command(BaseCommand):
    help = "reade info about client"
    def handle(self, *args, **options):
        client = Client.objects.all()
        self.stdout.write(str(client))