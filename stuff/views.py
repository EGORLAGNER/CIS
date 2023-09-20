from django.shortcuts import render
from django.views.generic import View

from stuff.models import *


class Index(View):
    """Заглавная страница приложения"""

    def get(self, request):
        text = 'This my CIS - "Corporate Information System"'
        context = {'context': text}
        return render(request, 'stuff/main_page.html', context)


class AllWorkers(View):
    """Показывает всех работников"""

    def get(self, request):
        all_workers = Worker.objects.all()
        context = {'workers': all_workers}
        return render(request, 'stuff/all_workers.html', context)
