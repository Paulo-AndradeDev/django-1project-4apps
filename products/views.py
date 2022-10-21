from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

def error404(request, exception): #aparecerá apenas com DEBUG = False (produção)
    return render(request, 'products/404.html')

def error500(request): #aparecerá apenas com DEBUG = False (produção)
    return render(request, 'products/500.html')

def produto(request, pk):
    #produto = Produto.objects.get(id = pk)
    produto = get_object_or_404(Produto,id = pk)
    contexto = {
        'prod': produto,
    }
    print(produto)
    return render(request, 'products/produto.html',contexto)


def index(request):
    produtos = Produto.objects.all()

    contexto = {
        'produtos' : produtos,
        'curso': 'Programação web com Python Django',
        'outro' : 'Geek University',
    }

    return render(request, 'products/index.html', contexto)






#from django.http import HttpResponse
#def index(request):
#return HttpResponse("Hello, world. You're at the polls index.")
