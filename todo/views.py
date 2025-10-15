from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    csrf_token = request.META.get("CSRF_COOKIE", "")
    return HttpResponse(
        f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Todo App</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .welcome {{ background: #e9ecef; padding: 20px; border-radius: 5px; }}
            .nav {{ margin: 20px 0; }}
            .nav a {{ margin-right: 15px; text-decoration: none; color: #007bff; }}
            .logout-form {{ display: inline; }}
            .logout-btn {{ background: none; border: none; color: #007bff; cursor: pointer; text-decoration: underline; font-size: inherit; }}
        </style>
    </head>
    <body>
        <div class="welcome">
            <h1>🚀 Приложение Todo</h1>
            <p>Добро пожаловать, <strong>{request.user.username}</strong>!</p>
        </div>

        <div class="nav">
            <a href="/">Главная</a>
            <a href="/accounts/dashboard/">Панель управления</a>
            <!-- Используем форму для выхода -->
            <form method="post" action="/accounts/logout/" class="logout-form">
                <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                <button type="submit" class="logout-btn">Выйти</button>
            </form>
        </div>

        <h2>Ваши задачи:</h2>
        <p>Здесь будет список ваших задач...</p>
    </body>
    </html>
    """
    )
