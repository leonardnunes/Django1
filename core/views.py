from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto


def index(request):
    produtos = Produto.objects.all()

    context = {
        'Curso': 'Programação em Python Web com Django Framework',
        'Outro': 'Django é massa!!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_list_or_404(Produto, id=pk)
    context = {
        'produto': prod
    }

    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request, ex):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)