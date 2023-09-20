from django.shortcuts import HttpResponse, render
from django.views.generic import View

from stuff.models import *


def index(request):
    """Заглавная страница приложения. Отображает название приложения"""
    return HttpResponse('This my CIS - "Corporate Information System"')


class AllWorkers(View):
    """Показывает всех работников"""

    def get(self, request):
        all_workers = Worker.objects.all()
        context = {'workers': all_workers}
        return render(request, 'stuff/index.html', context)
