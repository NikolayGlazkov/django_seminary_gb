from django.shortcuts import render
from django.http import HttpResponse

#индекс стартовая страница
def index(request):
    return HttpResponse("helloworld")
# Create your views here.
