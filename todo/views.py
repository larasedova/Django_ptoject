from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """
    <h1>Приложение Todo</h1>
    <p>Приложение для управления задачами работает корректно!</p>
    <p><a href="/">Вернуться на главную</a></p>
    """
    )
