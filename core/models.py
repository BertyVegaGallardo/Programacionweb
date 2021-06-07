from django.db import models


# Create your models here.


class Formulario_Persona(models.Model):
    rut = models.CharField(max_length=9,primary_key=True, verbose_name='Rut sin punto ni guión')
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    Apellido_paterno = models.CharField(max_length=40, verbose_name='Apellido Paterno')
    Apellido_materno = models.CharField(max_length=40, verbose_name='Apellido Materno')
    edad = models.IntegerField(verbose_name='Edad ')
    sexo = models.CharField(max_length=50, verbose_name='Sexo')

    def __str__(self):
        return self.rut
class Registro(models.Model):
    Nombre = models.CharField(max_length=40, verbose_name='nombre')
    apellidos = models.CharField(max_length=70, verbose_name='apellidos')
    correo = models.CharField(max_length=90, verbose_name='correo')
    contrasenia = models.CharField(max_length=100, verbose_name='contraseña')
   
    def __str__(self):
        return self.Nombre


