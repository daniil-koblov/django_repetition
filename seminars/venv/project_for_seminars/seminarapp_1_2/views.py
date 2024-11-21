from django.shortcuts import render
import random
import logging
from django.http import HttpResponse

# Create your views here.

logger = logging.getLogger(__name__)


def home(request):
    logger.info('Home page accessed')
    return HttpResponse(f"<h1>Добро пожаловать на страницу случайных "
                        f"игр.</h1>")


def flip_coin(request, tryes: int):
    logger.info("Coin page accessed")
    flips_list = [random.choice(["Орёл", "Решка"]) for _ in range(tryes)]
    context = {"title": "Flip coin", "content": flips_list}
    return render(request, "seminarapp_1_2/games.html", context)


def random_roll(request, tryes: int):
    logger.info('Random_roll page accessed')
    roll_list = [random.randint(1, 6) for _ in range(tryes)]
    context = {"title": "Random roll", "content": roll_list}
    return render(request, "seminarapp_1_2/games.html", context)


def random_number(request, tryes: int):
    logger.info('Random_number page accessed')
    number_list = [random.randint(1, 100) for _ in range(tryes)]
    context = {"title": "Random number", "content": number_list}
    return render(request, "seminarapp_1_2/games.html", context)
