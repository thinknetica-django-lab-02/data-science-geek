from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template_name = 'main/index.html'
    return HttpResponse(render(request, template_name))
