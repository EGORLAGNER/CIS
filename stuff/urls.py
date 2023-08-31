from django.urls import path
from stuff.views import index

urlpatterns = [
    path('', index),
]
