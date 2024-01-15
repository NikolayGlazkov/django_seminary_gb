# views.py
from django.shortcuts import render
from django.http import HttpResponse
import logging

# Настройка логгера
logger = logging.getLogger(__name__)


def index(request):
    # HTML-вёрстка и данные о вашем сайте
    site_info = """<h2>Добро пожаловать на мой первый Django-сайт!<br>меня зовут Николай мне 32 года<br>я много пропускаю но смотрю все в записи))</h2>"""

    # Сохраняем данные в лог
    logger.info("Посещена главная страница")

    # Возвращаем текстовый ответ
    return HttpResponse(site_info)
