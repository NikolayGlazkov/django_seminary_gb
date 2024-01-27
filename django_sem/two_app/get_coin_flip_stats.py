# two_app/get_coin_flip_stats.py
from .models import Counter

def get_coin_flip_stats(last_n_flips):
    recent_flips = Counter.objects.order_by('-id')[:last_n_flips]

    stats = {"face": 0, "back": 0}
    for flip in recent_flips:
        if flip.result == "face":
            stats["face"] += 1
        elif flip.result == "back":
            stats["back"] += 1

    return stats
