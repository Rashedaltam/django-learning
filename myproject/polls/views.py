from django.shortcuts import render
from django.http import HttpResponse

def myIndex(request):
    return HttpResponse("Hello, world. You're at the polls index.")
