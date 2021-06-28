from django.urls import path
from rest_bicicletas.views import lista_personas, detalle_bicicletas
from rest_bicicletas.viewsLogin import login

urlpatterns =[
    path('lista_personas', lista_personas, name="lista_personas"),
    path('detalle_bicicletas/<id>', detalle_bicicletas, name="detalle_bicicletas"),
    path('login',login, name="login"),
]

