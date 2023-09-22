from django.shortcuts import render
from django.views.generic import View

from core.models import *


class Index(View):
    """Заглавная страница приложения"""

    def get(self, request):
        text = 'This my CIS - "Corporate Information System"'
        context = {'context': text}
        return render(request, 'stuff/main_page.html', context)


class AllWorkers(View):
    """Показывает всех работников"""

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            workers = Employee.objects.filter(last_name__icontains=search_query)
        else:
            workers = Employee.objects.all()
        context = {'workers': workers}

        return render(request, 'stuff/all_workers.html', context)
