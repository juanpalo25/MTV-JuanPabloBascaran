from django.http import HttpResponse
from desafio.models import Familia
from django.template import loader
from django.shortcuts import render


def una_vista(request):
    return HttpResponse('<h1>Bienvenido</h1>')

def mi_template(request):
    template = loader.get_template('index.html')
    prueba1= """ACA IRIA EL NOMBRE DE LA CLASE, QUE NO LO RECONOCE"""(nombre='Laura')
    prueba2= """ACA IRIA EL NOMBRE DE LA CLASE, QUE NO LO RECONOCE"""(nombre='Florencia')
    prueba3= """ACA IRIA EL NOMBRE DE LA CLASE, QUE NO LO RECONOCE"""(nombre='Gaston')
    
    render = template.render({'lista de objetos': [prueba1, prueba2, prueba3] })
    return HttpResponse(render)