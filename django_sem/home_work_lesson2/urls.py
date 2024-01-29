from django.urls import path
from .views import (
    client_index, client_create, client_edit, client_delete,
    product_index, product_create, product_edit, product_delete,
)

urlpatterns = [
    # Маршруты для клиентов
    path('clients/', client_index, name='client_index'),
    path('clients/create/', client_create, name='create_client'),
    path('clients/<int:id>/edit/', client_edit, name='edit_client'),
    path('clients/<int:id>/delete/', client_delete, name='delete_client'),

    # Маршруты для товаров
    path('products/', product_index, name='product_index'),
    path('products/create/', product_create, name='create_product'),
    path('products/<int:id>/edit/', product_edit, name='edit_product'),
    path('products/<int:id>/delete/', product_delete, name='delete_product'),
]
