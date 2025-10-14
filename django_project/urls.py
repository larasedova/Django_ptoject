from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


def home(request):
    user_info = ""
    if request.user.is_authenticated:
        user_info = f"""
        <div style="background: #e9ecef; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
            <p>Вы вошли как <strong>{request.user.username}</strong></p>
            <form method="post" action="/accounts/logout/">
                <input type="hidden" name="csrfmiddlewaretoken" value="{request.META.get('CSRF_COOKIE', '')}">
                <button type="submit" style="background: #dc3545; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">Выйти</button>
            </form>
        </div>
        """
    else:
        user_info = """
        <div class="auth-links">
            <a href="/accounts/login/">Войти</a> | 
            <a href="/accounts/register/">Зарегистрироваться</a>
        </div>
        """

    return HttpResponse(
        f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }}
            .container {{ text-align: center; }}
            .nav {{ margin: 30px 0; }}
            .nav a {{ display: inline-block; margin: 0 10px; padding: 10px 20px; 
                     text-decoration: none; background: #007bff; color: white; 
                     border-radius: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Добро пожаловать в Django Todo приложение!</h1>
            <p>Простое приложение для управления задачами с системой аутентификации</p>
            
            {user_info}
            
            <div class="nav">
                <a href="/todo/">Приложение Todo</a>
                <a href="/admin/">Админка</a>
                <a href="/accounts/dashboard/">Панель управления</a>
            </div>
        </div>
    </body>
    </html>
    """
    )


# ОПРЕДЕЛЯЕМ urlpatterns ОДИН РАЗ В КОНЦЕ ФАЙЛА
urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
    path("accounts/", include("accounts.urls")),
    path("", home, name="home"),
]
