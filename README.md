# Django Todo Application с Аутентификацией
Простое приложение для управления задачами, созданное на Django с системой аутентификации и CI/CD пайплайном.

## 📋 Функциональность

Основная функциональность
✅ Создание, редактирование и удаление задач

✅ Отметка задач как выполненных

✅ Админ-панель для управления задачами

Система аутентификации
✅ Регистрация новых пользователей

✅ Вход в систему (LoginView)

✅ Выход из системы (LogoutView)

✅ Защищенные страницы с декоратором @login_required

✅ Панель управления для авторизованных пользователей

✅ Проверка прав доступа к защищенным страницам

## 🛠 Технологии

- Python 3.10+
- Django 5.2+
- SQLite (разработка)
- Django ORM
- Django Authentication System
- GitHub Actions (CI/CD)


🚀 Быстрый старт
1. Клонирование репозитория
```
git clone https://github.com/larasedova/Django_ptoject.git
cd Django_ptoject
```
2. Настройка виртуального окружения
```
# Создание виртуального окружения
python -m venv django_env

# Активация (Windows)
django_env\Scripts\activate

# Активация (Mac/Linux)
source django_env/bin/activate
```
3. Установка зависимостей
```
pip install -r requirements.txt
```
4. Настройка базы данных
```
# Применение миграций
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser
```
5. Загрузка демонстрационных данных
```
# Загрузка фикстур с демонстрационными данными
python manage.py loaddata tasks
```
6. Запуск сервера
```
python manage.py runserver
```
🌐 Доступные страницы
Главная страница: http://127.0.0.1:8000/

Регистрация: http://127.0.0.1:8000/accounts/register/

Вход в систему: http://127.0.0.1:8000/accounts/login/

Панель управления: http://127.0.0.1:8000/accounts/dashboard/

Приложение Todo: http://127.0.0.1:8000/todo/ (только для авторизованных)

Админ-панель: http://127.0.0.1:8000/admin/

🔐 Система аутентификации
Реализованные функции:
1. Регистрация пользователей
Использован CreateView с UserCreationForm

Поля: имя пользователя, пароль, подтверждение пароля

Автоматический редирект на страницу входа после регистрации

2. Вход в систему
Использован LoginView с кастомным шаблоном

Проверка учетных данных

Редирект на защищенную панель управления

3. Выход из системы
Использован LogoutView

Подтверждение выхода

Редирект на главную страницу

4. Защищенные страницы
Декоратор @login_required для ограничения доступа

Автоматический редирект на страницу входа для неавторизованных пользователей

Панель управления и приложение Todo доступны только после аутентификации

Маршруты аутентификации:
```
/accounts/register/     - Регистрация нового пользователя
/accounts/login/        - Вход в систему  
/accounts/logout/       - Выход из системы
/accounts/dashboard/    - Защищенная панель управления
```
🗃 Модель данных
Task
```
| Поле          | Тип            | Описание                               |
|---------------|----------------|----------------------------------------|
| `title`       | CharField(200) | Название задачи                        |
| `description` | TextField      | Описание задачи                        |
| `completed`   | BooleanField   | Статус выполнения (по умолчанию False) |
| `created_at`  | DateTimeField  | Дата создания (автоматически)          |
```
User (встроенная модель Django)
Используется стандартная модель пользователя Django

Поддержка аутентификации и авторизации

🔒 Защита приложения
Проверки безопасности:
✅ Защищенные страницы недоступны без аутентификации

✅ Автоматический редирект на страницу входа

✅ CSRF защита для всех форм

✅ Валидация паролей (минимальная длина 8 символов)

✅ Безопасные сессии с настройкой времени жизни

🤖 CI/CD Автоматизация
GitHub Actions пайплайн (.github/workflows/ci.yml)
Триггеры:
При push в ветки: main, master, develop

При создании pull request

Выполняемые проверки:
Job: Test and Lint

✅ Тестирование на Python 3.9, 3.10, 3.11

✅ Проверка синтаксиса кода с flake8

✅ Запуск миграций базы данных

✅ Выполнение Django тестов (python manage.py test)

✅ Запуск тестов через pytest

✅ Проверка покрытия кода тестами (coverage)

Job: Security Check

✅ Сканирование кода на уязвимости (Bandit)

✅ Проверка зависимостей на известные уязвимости (Safety)

Настройки линтера (flake8)
```
max-line-length = 127
max-complexity = 10
exclude = .git,__pycache__,migrations
```
📊 Демонстрационные данные
После загрузки фикстур в базе данных будут 2 задачи, демонстрирующие CRUD операции:

"Изучить Django ORM" - ✅ ВЫПОЛНЕНО

Демонстрация операции UPDATE (изменение статуса)

"Создать todo приложение" - ⏳ АКТИВНА

Демонстрация операции CREATE (создание задачи)

"Написать тесты" - ❌ УДАЛЕНА

Демонстрация операции DELETE (удаление задачи)

💻 Работа с Django ORM
Примеры использования в Django shell
```
python manage.py shell
python
from todo.models import Task
from django.contrib.auth.models import User
```

# Создание задачи
```
task = Task.objects.create(
    title="Новая задача",
    description="Описание новой задачи"
)

# Получение всех задач
all_tasks = Task.objects.all()

# Фильтрация задач
completed_tasks = Task.objects.filter(completed=True)
active_tasks = Task.objects.filter(completed=False)

# Работа с пользователями
user = User.objects.create_user(
    username='testuser',
    password='testpass123'
)
```

## 📁 Структура проекта
```
django_project/
├── .github/                          # Новая папка для CI/CD
│   └── workflows/
│       └── ci.yml                    # Файл CI/CD pipeline
├── accounts/                         
│   ├── __init__.py
│   ├── apps.py                       # Конфигурация приложения
│   ├── migrations/                   # Миграции (если будут свои модели)
│   │   └── __init__.py
│   ├── urls.py                       # URL-адреса аутентификации
│   └── views.py                      
├── django_project/                   # Настройки проекта
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                   # Обновленный файл настроек
│   ├── urls.py                       # Обновленный главный urls.py
│   └── wsgi.py
├── templates/                        
│   ├── registration/                 # Папка для шаблонов аутентификации
│   │   ├── login.html                # ← Шаблон входа
│   │   ├── logged_out.html           # ← Шаблон выхода
│   │   └── register.html             # ← Шаблон регистрации
│   └── dashboard.html                # ← Шаблон панели управления
├── todo/                             # Существующее приложение Todo
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures/
│   │   ├── tasks.json
│   │   └── README.md
│   ├── migrations/          		 # Миграции базы данных
│   ├── models.py            		 # Модель Task
│   ├── tests.py
│   ├── urls.py              		 # URL-адреса приложения
│   └── views.py                     # Обновленный - с @login_required
├── .flake8                          # Новый файл - конфигурация flake8
├── .gitignore              		 # Исключения для Git
├── db.sqlite3             	         # База данных (локальная)
├── manage.py              		     # Утилита управления
├── README.md              		     # Документация
└── requirements.txt                 # Обновленный - с новыми зависимостями
```

## 🔧 Команды управления

```
# Запуск сервера разработки
python manage.py runserver

# Создание миграций
python manage.py makemigrations

# Применение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Загрузка демонстрационных данных
python manage.py loaddata tasks

# Запуск тестов
python manage.py test

# Проверка стиля кода
flake8 .

# Запуск pytest
pytest
```

## 📝 Выполненные задачи проекта

### ✅ Задача 1: Создание приложения Django
- Создан проект Django
- Добавлено приложение `todo`
- Настроены URL-адреса
- Проверена корректная работа сервера

### ✅ Задача 2: Создание модели и миграций
- Создана модель `Task` с полями:
  - `title` (CharField)
  - `description` (TextField) 
  - `completed` (BooleanField)
  - `created_at` (DateTimeField)
- Выполнены миграции базы данных
- Модель зарегистрирована в админ-панели

### ✅ Задача 3: Работа с данными через Django ORM
- Создано 3 объекта Task через Django shell
- Выполнены операции:
  - **CREATE** - создание задач
  - **READ** - получение всех задач
  - **UPDATE** - изменение статуса задачи
  - **DELETE** - удаление задачи
- Демонстрационные данные сохранены в фикстуры

## 🐛 Решение проблем

### Ошибка: "no such table: django_session"
```
python manage.py migrate
```

### Ошибка: "ModuleNotFoundError: No module named 'django'"
```
# Активируйте виртуальное окружение
django_env\Scripts\activate  # Windows
source django_env/bin/activate  # Mac/Linux
```

### Ошибка порта уже используется
```
python manage.py runserver 8001
```

## 👥 Разработка

### Добавление новых функций
1. Создайте миграции для изменений моделей
2. Напишите тесты для новой функциональности
3. Протестируйте изменения локально
4. Создайте pull request для автоматической проверки

## Структура коммитов
```
feat: - новая функциональность
fix: - исправление ошибок
docs: - обновление документации
refactor: - рефакторинг кода
```
## 📄 Лицензия

Этот проект создан в учебных целях для демонстрации работы с Django ORM, системой аутентификации и CI/CD пайплайнами.

---

**Автор**: Larisa Sedova  
**Проект**: Django Todo Application с Аутентификацией  
**Дата**: Октябрь 2025
# CI test 
