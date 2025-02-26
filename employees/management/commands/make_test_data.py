import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from employees.models import Employee, Department


class Command(BaseCommand):
    help = 'Создаю тестовые данныю.'

    def handle(self, *args, **options):
        Department.objects.all().delete()
        Employee.objects.all().delete()

        departments = []

        # Создание департаментов
        for i in range(25):
            parent = random.choice(departments[:5]) if departments else None
            department = Department.objects.create(
                name=f'Подразделение {i + 1}',
                parent=parent,
            )
            departments.append(department)

        positions = ['Менеджер', 'Оператор', 'Грузчик', 'Байер', 'Тестировщик',
                     'Управляющий', 'Разработчик', 'Водитель', 'Работник']

        # Создаем сотрудников
        for i in range(50000):
            Employee.objects.create(
                full_name=f'Сотрудник {i + 1}',
                position=random.choice(positions),
                hire_date=date.today() - timedelta(
                    days=random.randint(1, 3650)),
                salary=random.randint(50000, 200000),
                department=random.choice(departments)
            )
        self.stdout.write(self.style.SUCCESS("Test data completed!"))
