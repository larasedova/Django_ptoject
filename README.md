# Django Todo Application

Простое приложение для управления задачами, созданное на Django с использованием Django ORM.

## 📋 Функциональность

- ✅ Создание, редактирование и удаление задач
- ✅ Отметка задач как выполненных
- ✅ Админ-панель для управления задачами
- ✅ Модель Task с полями: название, описание, статус выполнения, дата создания
- ✅ Полная демонстрация CRUD операций через Django ORM

## 🛠 Технологии

- Python 3.8+
- Django 5.2+
- SQLite (разработка)
- Django ORM

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```
git clone https://github.com/larasedova/Django_ptoject.git
cd Django_ptoject
```

### 2. Настройка виртуального окружения

```
# Создание виртуального окружения
python -m venv django_env

# Активация (Windows)
django_env\Scripts\activate

# Активация (Mac/Linux)
source django_env/bin/activate
```

### 3. Установка зависимостей

```
pip install -r requirements.txt
```

### 4. Настройка базы данных

```
# Применение миграций
python manage.py migrate

# Создание суперпользователя (опционально)
python manage.py createsuperuser
```

### 5. Загрузка демонстрационных данных

```
# Загрузка фикстур с демонстрационными данными
python manage.py loaddata tasks
```

### 6. Запуск сервера

```
python manage.py runserver
```

## 🌐 Доступные страницы

- **Главная страница**: http://127.0.0.1:8000/
- **Приложение Todo**: http://127.0.0.1:8000/todo/
- **Админ-панель**: http://127.0.0.1:8000/admin/

## 📊 Демонстрационные данные

После загрузки фикстур в базе данных будут 2 задачи, демонстрирующие CRUD операции:

1. **"Изучить Django ORM"** - ✅ ВЫПОЛНЕНО
   - Демонстрация операции UPDATE (изменение статуса)

2. **"Создать todo приложение"** - ⏳ АКТИВНА  
   - Демонстрация операции CREATE (создание задачи)

3. **"Написать тесты"** - ❌ УДАЛЕНА
   - Демонстрация операции DELETE (удаление задачи)

## 🗃 Модель данных

### Task
```
| Поле          | Тип            | Описание                               |
|---------------|----------------|----------------------------------------|
| `title`       | CharField(200) | Название задачи                        |
| `description` | TextField      | Описание задачи                        |
| `completed`   | BooleanField   | Статус выполнения (по умолчанию False) |
| `created_at`  | DateTimeField  | Дата создания (автоматически)          |
```

## 💻 Работа с Django ORM

### Примеры использования в Django shell

```
python manage.py shell
```

```
from todo.models import Task
from django.utils import timezone

# Создание задачи
task = Task.objects.create(
    title="Новая задача",
    description="Описание новой задачи"
)

# Получение всех задач
all_tasks = Task.objects.all()

# Фильтрация задач
completed_tasks = Task.objects.filter(completed=True)
active_tasks = Task.objects.filter(completed=False)

# Обновление задачи
task = Task.objects.get(title="Изучить Django ORM")
task.completed = True
task.save()

# Удаление задачи
task = Task.objects.get(title="Написать тесты")
task.delete()
```

## 📁 Структура проекта

```
django_project/
├── django_project/          # Настройки проекта
│   ├── __init__.py
│   ├── settings.py          # Конфигурация
│   ├── urls.py              # Главные URL-адреса
│   └── wsgi.py              # WSGI конфигурация
├── todo/                    # Приложение Todo
│   ├── __init__.py
│   ├── admin.py             # Настройка админ-панели
│   ├── apps.py
│   ├── fixtures/            # Демонстрационные данные
│   │   ├── tasks.json
│   │   └── README.md
│   ├── migrations/          # Миграции базы данных
│   ├── models.py            # Модель Task
│   ├── tests.py
│   ├── urls.py              # URL-адреса приложения
│   └── views.py             # Представления
├── .gitignore               # Исключения для Git
├── db.sqlite3               # База данных (локальная)
├── manage.py                # Утилита управления
├── README.md                # Документация
└── requirements.txt         # Зависимости проекта
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

# Запуск Django shell
python manage.py shell
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
2. Протестируйте изменения
3. Создайте фикстуры для демонстрационных данных
4. Обновите документацию

## Структура коммитов
```
feat: - новая функциональность
fix: - исправление ошибок
docs: - обновление документации
refactor: - рефакторинг кода
```
## 📄 Лицензия

Этот проект создан в учебных целях для демонстрации работы с Django ORM.

---

**Автор**: Larisa Sedova  
**Проект**: Django Todo Application  
**Дата**: Октябрь 2025
