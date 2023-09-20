from django.contrib import admin

from stuff.models import *

"""Подключение моделей к стандартной админ панели для возможностей создания, редактирования, удаления"""
admin.site.register(Worker)
admin.site.register(Department)
