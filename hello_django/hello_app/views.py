from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def create2(request):
    return HttpResponse("<b>hello world</b>")

def create3(request):
    return render(request,'hello.html')

def create(request):
    move
    
    return render(request,'hello.html')