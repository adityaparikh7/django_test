from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_django(request):
    return HttpResponse("Hello, Django!")
