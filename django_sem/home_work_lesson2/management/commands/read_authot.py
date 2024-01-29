from django.core.management import BaseCommand
from two_app.models import Author


class Command(BaseCommand):
    help = "reade info about user"
    def handle(self, *args, **options):
        author = Author.objects.all()
        self.stdout.write(str(author))