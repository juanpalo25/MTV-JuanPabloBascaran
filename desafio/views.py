from django.http import HttpResponse
from desafio.models import Familia
from django.template import loader
from django.shortcuts import render


def una_vista(request):
    return HttpResponse('<h1>Bienvenido</h1>')

def mi_template(request):
    template = loader.get_template('index.html')
    modelo1= Familia(nombre='Laura', anios= 49)
    modelo1.save()
    modelo2= Familia(nombre='Florencia', anios= 25)
    modelo2.save()
    modelo3= Familia(nombre='Gaston', anios= 36)
    modelo3.save()
    lista_familiares = Familia.objects.all()
    
    render = template.render({'lista_familiares': lista_familiares})
    return HttpResponse(render)