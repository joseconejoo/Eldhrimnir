from django.db import models

from django.contrib.auth.models import User

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class NivelesNum2(models.Model):
	nivel_num = models.IntegerField(primary_key = True, unique= True)
	nom_nivel = models.CharField(max_length=200)
	def __str__(self):
		return str(self.nom_nivel)

class NivelUsu(models.Model):
	user = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
	nivel_usu = models.ForeignKey(NivelesNum2,on_delete=models.CASCADE, blank=True)
   
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
	residencia = models.CharField(max_length=200, null=True)

class carreras(models.Model):
	nombVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
	nombre = models.CharField(validators=[nombVer],max_length=200)
	user_edit = models.ForeignKey('auth.User',on_delete=models.SET_NULL, blank=True, null= True)
	date_edit = models.DateTimeField(blank=True)

class carrera_seccion(models.Model):
	seccion_num = models.IntegerField()
	carrera = models.ForeignKey(carreras,on_delete=models.CASCADE, blank=True)
	user_edit = models.ForeignKey('auth.User',on_delete=models.SET_NULL, blank=True, null = True)
	date_edit = models.DateTimeField(blank=True)

class Tipo_Materia(models.Model):
	id1 = models.IntegerField(primary_key = True, unique = True)
	nombreVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
	Nombre = models.CharField(validators = [nombreVer], max_length = 200)
	num_eval_min = models.IntegerField()
	def __str__(self):
	    return str((self.Nombre))

class materia_seccion(models.Model):
	nombreVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
	materia_nom = models.CharField(validators=[nombreVer],max_length=200)
	seccion = models.ForeignKey(carrera_seccion, on_delete=models.CASCADE, blank=True)
	#profesor = models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True, related_name = 'profesors')
	user_edit = models.ForeignKey('auth.User',on_delete=models.SET_NULL, blank=True, related_name = 'user_edits', null = True)
	date_edit = models.DateTimeField(blank=True)
	tipo_mate = models.ForeignKey(Tipo_Materia, on_delete = models.CASCADE)


class MateriasEstu(models.Model):
	student = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	materia = models.ForeignKey(materia_seccion,on_delete=models.CASCADE)

class MateriaTeacher(models.Model):
	materia = models.OneToOneField(materia_seccion, on_delete=models.CASCADE)
	profesor = models.ForeignKey('auth.User', on_delete= models.CASCADE, null=True)

class evaluacion_materia(models.Model):
	materia = models.ForeignKey(materia_seccion, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=250)
	ponderacion = models.PositiveIntegerField(validators=[MinValueValidator(5,message="Ponderación no valida."), MaxValueValidator(30,message="Ponderación no valida.")])
	fecha = models.DateField(blank=True)

class eval_estudiante(models.Model):
	student = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	evaluacion_num = models.ForeignKey(evaluacion_materia, on_delete=models.CASCADE)
	nota = models.PositiveIntegerField()
	asistente = models.BooleanField(default=False)