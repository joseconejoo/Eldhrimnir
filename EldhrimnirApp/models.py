from django.db import models

from django.contrib.auth.models import User

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.


class NivelesNum(models.Model):
	usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
	coord = models.BooleanField(default=False)
	ctrl_est1 = models.BooleanField(default=False)
	prof = models.BooleanField(default=False)
	estud = models.BooleanField(default=False)

class Datos1(models.Model):
	usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
	nombVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
	nombre = models.CharField(validators=[nombVer],max_length=200)
	apellVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el apellido por favor.")
	apellido = models.CharField(validators=[apellVer],max_length=200)
	fedicion = models.DateTimeField(blank=True, null=True)
	email = models.EmailField(null=True)
	residencia = models.CharField(max_length=200)

class carreras(models.Model):
	nombVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
	nombre = models.CharField(validators=[nombVer],max_length=200)
	user_edit = models.ForeignKey('auth.User',on_delete=models.CASCADE, blank=True)
	date_edit = models.DateTimeField(blank=True)

class carrera_seccion(models.Model):
	seccion_num = models.IntegerField(unique= True)
	carrera = models.ForeignKey(carreras,on_delete=models.CASCADE, blank=True)
	user_edit = models.ForeignKey('auth.User',on_delete=models.CASCADE, blank=True)
	date_edit = models.DateTimeField(blank=True)

class materia_seccion(models.Model):
	nombreVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
	materia_nom = models.CharField(validators=[nombreVer],max_length=200)
	seccion = models.ForeignKey(carrera_seccion, on_delete=models.CASCADE, blank=True)
	profesor = models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True, related_name = 'profesors')
	user_edit = models.ForeignKey('auth.User',on_delete=models.CASCADE, blank=True, related_name = 'user_edits')
	date_edit = models.DateTimeField(blank=True)