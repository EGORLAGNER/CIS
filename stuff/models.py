from django.db import models


class Department(models.Model):
    """Модель подразделения/отделения/участка/департамента"""
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location


class Worker(models.Model):
    """Модель трудоустроенного сотрудника"""
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    # email = models.EmailField()
    # phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"({self.last_name.title()} {self.first_name.title()})"

    class Meta:
        ordering = ['last_name']
