from django.shortcuts import render

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    return render(request,'seminar3/index.html',{"main":"asdasd","content_main":"asdasd"})

def about(request):
    return render(request,"seminar3/about.html")


