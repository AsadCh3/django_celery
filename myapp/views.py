from django.shortcuts import render, HttpResponse
from .tasks import add
# Create your views here.



def index(request):
    add.delay()
    return HttpResponse('Hello THis')