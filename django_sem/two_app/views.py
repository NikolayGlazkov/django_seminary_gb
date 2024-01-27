# two_app/views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import logging
from .models import Counter
from .get_coin_flip_stats import get_coin_flip_stats

loger = logging.getLogger(__name__)

def log(func):
    def wrapper(*args, **kwarhs):
        loger.info(f"The view function {func.__name__} was returned {(result := func(*args, **kwarhs))}")
        return result
    return wrapper

def coin(request):
    result = random.choice(["face", 'back'])
    Counter.objects.create(result=result)
    return HttpResponse(result)

def dice(request):
    return HttpResponse(random.randint(1, 6))

def get_coin_flip_stats_view(request, last_n_flips):
    stats = get_coin_flip_stats(last_n_flips)
    return JsonResponse(stats)
