from django.db import models


class Department(models.Model):
    """Модель подразделения/отделения/участка/департамента"""
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location


class Employee(models.Model):
    """Модель трудоустроенного сотрудника"""

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    employee_number = models.BigIntegerField(unique=True, default=None)

    # email = models.EmailField()
    # phone = models.CharField(max_length=20)

    """Отношения между моделями"""
    department = models.ForeignKey(
        'Department',  # главная модель с которой строятся отношения One to Many
        on_delete=models.SET_NULL,  # обязательный аргумент, поведение при удалении связанного экземпляра
        null=True,  # разрешает оставлять пустое поле в базе данных
        blank=True,  # разрешает оставлять пустое поле при заполнении форм (не имеет отношения к базе данных)
        related_name='employees'  # присваивает связанное имя (если явно не указывать, то сгенерируется автоматически)
    )

    def __str__(self):
        return f"({self.last_name.title()} {self.first_name.title()})"

    class Meta:
        ordering = ['last_name']


class Device(models.Model):
    """Модель устройства/оборудования необходимого для выполнения работы"""
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    special_device = models.BooleanField(default=False)
    inventory_number = models.PositiveBigIntegerField()
    employee = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='devices'
    )

    def __str__(self):
        return self.name
