from django.urls import path
from .views import index
from .views import disciplina
from .views import Noticias
from .views import QuienesSomos
from .views import contacto
from .views import Registrarse
from .views import Iniciarsesion
from .views import dj
from .views import xc
from .views import ruta
from .views import bmx
from .views import dh
from .views import Mariana
from .views import bosh
from .views import ciclista
from .views import FormularioPersona
from .views import form_mod_pers
from .views import form_del_pers
from .views import Test
from .views import Test2


urlpatterns = [    
    path('',index,name="index"),
    path('test',Test,name="test"),
    path('disciplina',disciplina,name="disciplina"),
    path('Noticias',Noticias,name="Noticias"),
    path('QuienesSomos',QuienesSomos,name="QuienesSomos"),
    path('contacto',contacto,name="contacto"),
    path('Registrarse',Registrarse,name="Registrarse"),
    path('dj',dj,name="dj"),
    path('xc',xc,name="xc"),
    path('ruta',ruta,name="ruta"),
    path('bmx',bmx,name="bmx"),
    path('dh',dh,name="dh"),
    path('Mariana',Mariana,name="Mariana"),
    path('bosh',bosh,name="bosh"),
    path('ciclista',ciclista,name="ciclista"),
    path('Iniciarsesion',Iniciarsesion,name="Iniciarsesion"),
    path('FormularioPersona',FormularioPersona,name="FormularioPersona"),
    path('form_mod_pers/<id>',form_mod_pers,name="form_mod_pers"),
    path('form_del_pers/<id>',form_del_pers,name="form_del_pers"),
    path('Test2', Test2, name="Test2"),


]