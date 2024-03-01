from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return HttpResponse("<h1>Bienvenido Developer</h1>")

def carga_index(request):
    return render(request, 'paginas/index.html')