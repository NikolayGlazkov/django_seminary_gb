from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from two_app.models import Author


class Command(BaseCommand):
    help = f"Delete user about user"

    def add_arguments(self, parser):
        parser.add_argument("fullname", type=str, help="The fullname Author to delete")

    def handle(self, *args, **options):
        full_name = options["fullname"]
        try:
            author = Author.objects.get(fullname=full_name)
            author.delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully deleted author with full name "{full_name}"'
                )
            )
        except Author.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Author with full name "{full_name}" does not exist')
            )
