from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Client, Product, Order

# Для клиентов
def client_index(request):
    clients = Client.objects.all()
    return render(request, "client_index.html", {"clients": clients})

def client_create(request):
    if request.method == "POST":
        # Создание нового клиента
        client = Client()
        client.name = request.POST.get("name")
        client.email = request.POST.get("email")
        client.number = request.POST.get("number")
        client.addres = request.POST.get("addres")
        client.registr_date = request.POST.get("registr_date")
        client.save()
        return HttpResponseRedirect("/clients")
    return render(request, "client_create.html")

def client_edit(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.name = request.POST.get("name")
        client.email = request.POST.get("email")
        client.number = request.POST.get("number")
        client.addres = request.POST.get("addres")
        client.registr_date = request.POST.get("registr_date")
        client.save()
        return redirect('client_index')
    return render(request, "client_edit.html", {"client": client})

def client_delete(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.delete()
        return redirect('client_index')
    return render(request, "client_delete.html", {"client": client})

# Для товаров
def product_index(request):
    products = Product.objects.all()
    return render(request, "product_index.html", {"products": products})

def product_create(request):
    if request.method == "POST":
        product = Product()
        product.product_name = request.POST.get("product_name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.quantity = request.POST.get("quantity")
        product.date = request.POST.get("date")
        product.save()
        return HttpResponseRedirect("/products")
    return render(request, "product_create.html")

def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.product_name = request.POST.get("product_name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.quantity = request.POST.get("quantity")
        product.date = request.POST.get("date")
        product.save()
        return redirect('product_index')
    return render(request, "product_edit.html", {"product": product})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect('product_index')
    return render(request, "product_delete.html", {"product": product})

# Для заказов
# Здесь вы можете добавить похожие функции для заказов
