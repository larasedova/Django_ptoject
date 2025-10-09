from django.test import TestCase
from django.utils import timezone
from .models import Task


class TaskModelTest(TestCase):

    def setUp(self):
        """Создаем тестовые данные"""
        self.task = Task.objects.create(
            title="Тестовая задача",
            description="Это описание тестовой задачи",
            completed=False,
        )

    def test_task_creation(self):
        """Тест создания задачи"""
        self.assertEqual(self.task.title, "Тестовая задача")
        self.assertEqual(self.task.description, "Это описание тестовой задачи")
        self.assertFalse(self.task.completed)
        self.assertIsNotNone(self.task.created_at)

    def test_task_string_representation(self):
        """Тест строкового представления задачи"""
        self.assertEqual(str(self.task), "Тестовая задача")

    def test_task_default_values(self):
        """Тест значений по умолчанию"""
        task = Task.objects.create(title="Задача без описания")
        self.assertFalse(task.completed)
        self.assertEqual(task.description, "")

    def test_task_completion(self):
        """Тест отметки задачи как выполненной"""
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)


class TaskCRUDTest(TestCase):

    def test_create_task(self):
        """Тест создания задачи через ORM"""
        task = Task.objects.create(
            title="Новая задача", description="Описание новой задачи"
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, "Новая задача")

    def test_read_task(self):
        """Тест чтения задачи"""
        task = Task.objects.create(title="Задача для чтения")
        retrieved_task = Task.objects.get(id=task.id)
        self.assertEqual(retrieved_task.title, "Задача для чтения")

    def test_update_task(self):
        """Тест обновления задачи"""
        task = Task.objects.create(title="Старое название")
        task.title = "Новое название"
        task.completed = True
        task.save()

        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.title, "Новое название")
        self.assertTrue(updated_task.completed)

    def test_delete_task(self):
        """Тест удаления задачи"""
        task = Task.objects.create(title="Задача для удаления")
        self.assertEqual(Task.objects.count(), 1)

        task.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_task_queryset(self):
        """Тест QuerySet операций"""
        # Создаем несколько задач
        Task.objects.create(title="Задача 1", completed=True)
        Task.objects.create(title="Задача 2", completed=False)
        Task.objects.create(title="Задача 3", completed=True)

        # Тестируем фильтрацию
        completed_tasks = Task.objects.filter(completed=True)
        self.assertEqual(completed_tasks.count(), 2)

        active_tasks = Task.objects.filter(completed=False)
        self.assertEqual(active_tasks.count(), 1)

        # Тестируем поиск
        search_result = Task.objects.filter(title__icontains="Задача")
        self.assertEqual(search_result.count(), 3)


class TaskViewsTest(TestCase):

    def test_todo_index_view(self):
        """Тест главной страницы приложения todo"""
        from django.test import Client
        from django.urls import reverse

        client = Client()
        response = client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Приложение Todo")

    def test_admin_access(self):
        """Тест доступа к админке"""
        from django.test import Client
        from django.urls import reverse

        client = Client()
        response = client.get("/admin/")

        # Должен быть редирект на страницу логина (302)
        self.assertEqual(response.status_code, 302)


class TaskIntegrationTest(TestCase):
    """Интеграционные тесты, имитирующие реальное использование"""

    def test_full_task_lifecycle(self):
        """Полный жизненный цикл задачи"""
        # CREATE - Создание
        task = Task.objects.create(
            title="Изучить тестирование в Django",
            description="Написать unit-тесты для моделей и представлений",
        )
        self.assertEqual(Task.objects.count(), 1)

        # READ - Чтение
        task_from_db = Task.objects.get(title="Изучить тестирование в Django")
        self.assertEqual(
            task_from_db.description, "Написать unit-тесты для моделей и представлений"
        )

        # UPDATE - Обновление
        task_from_db.completed = True
        task_from_db.save()
        self.assertTrue(Task.objects.get(id=task.id).completed)

        # DELETE - Удаление
        task_from_db.delete()
        self.assertEqual(Task.objects.count(), 0)
