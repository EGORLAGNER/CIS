from django.urls import path
from stuff.views import Index, AllWorkers

urlpatterns = [
    path('', Index.as_view(), name='main_page_url'),
    path('all_workers/', AllWorkers.as_view(), name='all_workers_url'),
]
