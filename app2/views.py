from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
def first_app2(request):
    return HttpResponse('<h1><marquee>This is first function of app2')

def second_app2(request):
    return HttpResponse('<h1><marquee>This is second function of app2')