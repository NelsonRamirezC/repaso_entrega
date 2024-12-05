from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Category


from .forms import CategoryForm

# Create your views here.

def categorias(request):
    contexto = {}
    
    contexto["categorias"] = Category.objects.all()
    return render(request, "categorias.html", contexto)


def categorias_add(request):
    contexto = {}
    
    if request.method == "GET":
        
        contexto["form"] = CategoryForm()

        return render(request, "categorias_add.html", contexto)
    
    if request.method == "POST":
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            pass