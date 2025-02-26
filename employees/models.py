from django.db import models
from django.core.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Название подразделения',
        help_text='Введите название подразделения'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='subdepartments',
        verbose_name='Родительское подразделение',
        help_text='Укажите родительское подразделение'
    )

    def clean(self):
        """ Проверяем, что глубина вложенности не превышает 5 уровней """
        depth = 1
        parent = self.parent
        while parent:
            depth += 1
            if depth > 5:
                raise ValidationError('Максимальная глубина '
                                      'подразделений – 5 уровней.')
            parent = parent.parent

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk', 'name']
        verbose_name = 'Подразделения'
        verbose_name_plural = 'Подразделения'


class Employee(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        help_text='Введите ФИО'
    )
    position = models.CharField(
        max_length=255,
        verbose_name='Должность',
        help_text='Укажите должность'
    )
    hire_date = models.DateField(
        verbose_name='Дата приема на работу',
        help_text='Укажите дату приема на работу'
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Размер заработной платы',
        help_text='Укажите размер заработной платы'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name='Подразделение',
        help_text='Укажите подразделение'
    )

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['pk', 'full_name']
        verbose_name = 'Работники'
        verbose_name_plural = 'Работники'
