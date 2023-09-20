from django.urls import path
from stuff.views import index, AllWorkers

urlpatterns = [
    path('', index),
    path('all_workers/', AllWorkers.as_view(), name='all_workers'),
]
