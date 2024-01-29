from django.core.management import BaseCommand
from two_app.models import Author


class Command(BaseCommand):
    help = "create user"
    def handle(self, *args, **options):
        author = Author(
            ferst_name="Nikolay",
            last_name="Glazkov",
            email="adasd@adsasd.ru",
            biograpt="i'm from Alekseevka",
            birthday="1991-08-07",
            
        )
        author.fullname = author.full_name()
        author.save()