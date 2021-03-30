from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template_name = 'main/index.html'
    context = {'turn_on_block': True}
    return HttpResponse(render(request, template_name, context=context))
