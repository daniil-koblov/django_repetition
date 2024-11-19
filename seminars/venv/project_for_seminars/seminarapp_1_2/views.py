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


def flip_coin(request):
    logger.info('Flip_coin page accessed')
    result = random.choice(['Орёл', 'Решка'])
    return HttpResponse(f'Результат подбрасывания монеты: <h1>{result}</h1>')


def random_roll(request):
    logger.info('Random_roll page accessed')
    result = random.randint(1, 6)
    return HttpResponse(f'После брока кубика выпало значение: <h1>'
                        f'{result}</h1>')


def random_number(request):
    logger.info('Random_number page accessed')
    result = random.randint(1, 100)
    return HttpResponse(f'Случайное значение от 1 до 100 равно: <h1>'
                        f'{result}</h1>')
