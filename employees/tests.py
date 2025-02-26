from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.urls import reverse
from employees.models import Department, Employee
from datetime import date


class DepartmentTestCase(TestCase):
    def setUp(self):
        """Создаём тестовые данные."""
        self.client = Client()
        self.department = Department.objects.create(
            name="Отдел продаж")
        self.employee = Employee.objects.create(
            full_name="Иван Иванов",
            position="Менеджер",
            hire_date=date(2022, 1, 15),
            salary=100000,
            department=self.department
        )

        # Создаём 5 уровней вложенных подразделений
        self.root = Department.objects.create(
            name="Уровень 1")
        self.level2 = Department.objects.create(
            name="Уровень 2", parent=self.root)
        self.level3 = Department.objects.create(
            name="Уровень 3", parent=self.level2)
        self.level4 = Department.objects.create(
            name="Уровень 4", parent=self.level3)
        self.level5 = Department.objects.create(
            name="Уровень 5", parent=self.level4)

    def test_department_tree_view(self):
        """Проверяем, что представление возвращает 200 OK."""
        url = reverse("employees:department_tree")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_cannot_create_sixth_level(self):
        """Проверяем, что нельзя создать 6-й уровень подразделений."""
        department = Department(
            name="Уровень 6", parent=self.level5)
        with self.assertRaises(ValidationError):
            department.clean()
            department.save()
