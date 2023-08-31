from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse('This my CIS - "Corporate Information System"')
