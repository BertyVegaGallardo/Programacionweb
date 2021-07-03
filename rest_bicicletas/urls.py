from django.urls import path
from rest_bicicletas.views import lista_personas, detalle_bicicletas,PersonaList



urlpatterns =[
    path('lista_personas', lista_personas, name="lista_personas"),
    path('detalle_bicicletas/<id>', detalle_bicicletas, name="detalle_bicicletas"),
    path('persona/',PersonaList.as_view(),name = 'persona_list'),
]


