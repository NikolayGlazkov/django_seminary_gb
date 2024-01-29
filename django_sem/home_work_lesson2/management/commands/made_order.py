from django.core.management import BaseCommand
from home_work_lesson2.models import Client, Product, Order

class Command(BaseCommand):
    help = "create order"

    def handle(self, *args, **options):
        # Получаем клиента из базы данных
        client = Client.objects.first()

        # Получаем продукты из базы данных
        products = Product.objects.all()

        # Создаем заказ и связываем его с клиентом
        order = Order.objects.create(
            client=client,
            total_amount=0,  # Начальное значение суммы заказа
            order_date='2022-01-29',
        )

        # Добавляем продукты к заказу и обновляем сумму заказа
        for product in products:
            order.products.add(product)
            order.total_amount += product.price

        order.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created order: {order.id}'))
