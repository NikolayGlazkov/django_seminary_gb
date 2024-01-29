from django.core.management import BaseCommand
from home_work_lesson2.models import Product

class Command(BaseCommand):
    help = "create Product"

    def handle(self, *args, **options):
        product = Product(
            product_name="snikers",
            description="shokolad",
            price="9.99",
            quantity="1000",
            date='2000-12-01',
        )
        product.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.product_name}'))
