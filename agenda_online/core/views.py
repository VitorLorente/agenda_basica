from django.shortcuts import render
from django.http import HttpResponse
from agenda_online.contatos.forms import ContatoForm
from agenda_online.contatos.models import Contato

def home(request):
    return render(request, 'index.html')

def adicionar(request):
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContatoForm()
    
    context = {
        'form' : form
    }
    return render(request, 'adicionar.html', context)

def pesquisa(request):
    return render(request, 'pesquisa.html')

def listar(request):
    contatos = Contato.objects.all()

    context = {
        'contatos' : contatos
    }
    return render(request, 'listar.html', context)

