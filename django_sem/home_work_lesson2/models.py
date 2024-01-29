from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=12)
    email = models.EmailField()
    number = models.CharField(max_length= 15)
    addres = models.TextField()
    registr_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.email}'
    

    
class Product(models.Model):
    product_name = models.CharField(max_length=12)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.product_name} - {self.description}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'Order {self.id} by {self.client.name}'
