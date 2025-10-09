from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # ← добавляем этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path("todo/", include("todo.urls")),  # ← ПОДКЛЮЧАЕМ URLs ПРИЛОЖЕНИЯ
]


# Простое представление для главной страницы
def home(request):
    return HttpResponse(
        """
    <h1>Добро пожаловать в Django Todo приложение!</h1>
    <p>Доступные страницы:</p>
    <ul>
        <li><a href="/todo/">Приложение Todo</a></li>
        <li><a href="/admin/">Админка</a></li>
    </ul>
    """
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path("", home, name="home"),  # ← добавляем маршрут для корневой страницы
]
