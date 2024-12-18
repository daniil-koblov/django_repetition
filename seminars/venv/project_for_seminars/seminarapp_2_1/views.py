from django.shortcuts import render
import random
import logging
from django.http import HttpResponse
from .models import CoinFlip

# Create your views here.

logger = logging.getLogger(__name__)


def home(request):
    logger.info('Home page accessed')
    return HttpResponse(f"<h1>Добро пожаловать на страницу случайных "
                        f"игр.</h1>")


def flip_coin_view(request):
    # result = random.choice(['heads', 'tails'])
    flip = CoinFlip.get_last_n_flips_stats(5)
    return render(request, 'seminarapp_2_1/coin_flip_template.html', {'flip': flip})
