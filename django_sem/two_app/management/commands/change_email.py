from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from two_app.models import Author


class Command(BaseCommand):
    help = "Update author details"

    def add_arguments(self, parser):
        parser.add_argument(
            "fullname", type=str, help="Full name of the author to update"
        )
        parser.add_argument("--first_name", type=str, help="New first name")
        parser.add_argument("--last_name", type=str, help="New last name")
        parser.add_argument("--email", type=str, help="New email")
        parser.add_argument("--biography", type=str, help="New biography")
        parser.add_argument("--birthday", type=str, help="New birthday")

    def handle(self, *args, **options):
        fullname = options["fullname"]
        updates = {
            k: v
            for k, v in options.items()
            if k in ["first_name", "last_name", "email", "biography", "birthday"]
            and v is not None
        }

        try:
            author = Author.objects.get(fullname=fullname)
        except Author.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'Author not found with full name "{fullname}"')
            )
            return

        for attr, value in updates.items():
            setattr(author, attr, value)

        author.fullname = (
            author.full_name()
        )  # Update fullname if first or last name changed
        author.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully updated details for author: {author.fullname}"
            )
        )
