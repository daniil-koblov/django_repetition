from django.shortcuts import render
import logging

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Главная страница",
        "content": "Приветствую на главной странице.",
    }
    logger.info("Index page accessed")
    return render(request, "hw_seminar_1/index.html", context)


def about(request):
    context = {
        "title": "О себе.",
    }
    logger.info("About page accessed")
    return render(request, "hw_seminar_1/about.html", context)
