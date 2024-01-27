from django.urls import path
from . import views

urlpatterns = [
    path("coin/",views.coin, name = 'coin'),
    path('dice/',views.dice,name='dice'),
    path('coin_stats/<int:last_n_flips>/', views.get_coin_flip_stats_view, name='coin_stats'),
]