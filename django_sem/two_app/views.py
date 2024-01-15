# two_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

loger = logging.getLogger(__name__)

def log(func):
    def wrapper(*args,**kwarhs):
        loger.info(f"The view function{func.__name__} was reterned {(result := func(*args,**kwarhs))}")
        return result
    return wrapper

def coin(request):
    return HttpResponse(random.choice(["face",'back']))

def dice(request):
    return HttpResponse(random.randint(1,6))

