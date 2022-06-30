from django.urls import path
from .views import una_vista, mi_template, vista_nueva

urlpatterns = [
    path('', una_vista, name= 'index'),
    path('mi-template', mi_template, ),
    path('vista-nueva', vista_nueva, name= 'vista_nueva')
]
    