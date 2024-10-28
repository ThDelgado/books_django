from django.shortcuts import render
from .models import Libros
from django.http import HttpResponse


# Create your views here.

def newbook(request):
    return render(request,"books/newbook.html", {})

def listbook(request):
    libros = Libros.objects.all()
    contexto = {}  
    contexto["libros"] = libros
    
    return render(request,"books/listbook.html", contexto)
