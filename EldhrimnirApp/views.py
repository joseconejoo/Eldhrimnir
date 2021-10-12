from django.shortcuts import render, redirect, get_object_or_404, resolve_url

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth import (
    authenticate, get_user_model, password_validation, backends
)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import Datos2rF, materias_listF, DatosAddF, materia_seccion_F, carrera_seccion_F, carreras_add, NivelesNumF1, DatosF, AuthenticationForm2, UserCreationForm2
from .models import MateriaTeacher, MateriasEstu, NivelesNum2, NivelUsu, materia_seccion, carrera_seccion ,carreras, Datos1, NivelesNum

from .func1 import prof_add_materia, est_add_materia

from django.contrib.auth.models import User

from django.utils import timezone


global nivel_estudiante
nivel_estudiante = 3
nivel_control_estudios = 1
nivel_profesor = 4

class login1(LoginView):
    template_name = 'login1.html'
    form_class = AuthenticationForm2

    def dispatch(self, request, *args, **kwargs):
        #migracion()
        if request.user.is_authenticated!=True:
            if self.redirect_authenticated_user and self.request.user.is_authenticated:
                redirect_to = self.get_success_url()
                return HttpResponseRedirect(redirect_to)
            return super().dispatch(request, *args, **kwargs)

        else:
            redirect_to = self.get_success_url()
            return HttpResponseRedirect(redirect_to)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def perfil_redirect(request):
	pk1 = User.objects.get(pk=request.user.pk)
	return redirect('perfil_u', pk=pk1.pk)


def perfil_u(request, pk):
	condition2 = Datos1.objects.filter(usuario=pk).exists()
	condition3 = False
	if (condition2):
		condition3 = Datos1.objects.get(usuario=pk).residencia
	#if (User.objects.filter(pk=pk).exists() and Datos1.objects.get(usuario=pk).residencia):
	if (User.objects.filter(pk=pk).exists() and (condition2 and condition3) ):
		usu1 = User.objects.get(pk=pk)
		dat1 = Datos1.objects.get(usuario=pk)
		niv1 = ''
		if NivelesNum.objects.filter(usuario=pk).exists():
			niv1 = NivelesNum.objects.get(usuario=pk)

		return render(request, 'perfil.html',{'niv1':niv1,'usu1':usu1,'dat1':dat1})
	else:
		#if (Datos1.objects.get(usuario=pk).nombre):
		print (condition2,'\n\n')
		if (condition2):

			if (Datos1.objects.get(usuario=pk).nombre):
				registred = True

		else:
			registred = False

		if request.method == "POST":
			if (registred):
				form2= Datos2rF(request.POST)
			else:
				form2= DatosF(request.POST)

			if form2.is_valid():
				post2 = form2.save(commit=False)
				post2.usuario = User.objects.get(pk=request.user.pk)
				if (registred):
					post2.save(update_fields=["residencia"])
					#new to edit info
				else:
					post2.save()
				#activate = True
				#messages.success(request, 'Registro Realizado exitosamente, Debe esperar la Aprobacion del Director')
				return redirect('perfil_u',pk=request.user.pk)

		else:
			if (registred):
				form2= Datos2rF()
			else:
				form2= DatosF()
		return render(request,'registros1.html', {'form2':form2, 'residencia1' : registred})

"""
def perfil_u(request, pk):
	try:
		usu1 = User.objects.get(pk=pk)
		dat1 = Datos1.objects.get(usuario=pk)
		niv1 = ''
		if NivelesNum.objects.filter(usuario=pk).exists():
			niv1 = NivelesNum.objects.get(usuario=pk)

		return render(request, 'perfil.html',{'niv1':niv1,'usu1':usu1,'dat1':dat1})
	except:
		if request.method == "POST":
		    form2= DatosF(request.POST)
		    
		    if form2.is_valid():
		    	post2 = form2.save(commit=False)
		    	post2.usuario = User.objects.get(pk=request.user.pk)
		    	post2.save()
		    	#activate = True
		    	#messages.success(request, 'Registro Realizado exitosamente, Debe esperar la Aprobacion del Director')
		    	return redirect('perfil_u',pk=request.user.pk)
		else:
		    form2 = DatosF()

		return render(request,'registros1.html', {'form2':form2})

"""
def registros1(request):
	#formlistoption = unidad2.objects.filter().order_by('id')
	if request.method == "POST":
	    foxr = UserCreationForm2(request.POST)
	    form2= DatosF(request.POST)
	    form3= NivelesNumF1()
	    
	    if foxr.is_valid() and form2.is_valid():

	    	#codd = request.POST.get('codigo')
	    	post = foxr.save(commit=False)
	    	#numero_nivel = request.POST.get('nivel_usua')
	    	post.is_active = 0
	    	post2 = form2.save(commit=False)
	    	post3 = form3.save(commit=False)
	    	"""
	    	lista_num =[1,2,3,4,5]
	    	if numero_nivel in lista_num:
	    	    post2.cod_area = unidad2.objects.get(pk=16)

	    	lista_coord = [2]
	    	if numero_nivel in lista_coord:
	    	    post.is_superuser=True
	    	"""

	    	post.save()
	    	post3.usuario = post
	    	post3.ctrl_est1 = True
	    	post2.usuario = post
	    	#usuario1 = User.objects.get(pk=post.pk)
	    	#post2.usuario=usuario1

	    	post2.save()
	    	post3.save()
	    	#activate = True
	    	#messages.success(request, 'Registro Realizado exitosamente, Debe esperar la Aprobacion del Director')
	    	return redirect('login1')
	else:
	    foxr = UserCreationForm2()
	    form2 = DatosF()

	return render(request,'registros1.html', {'form':foxr,'form2':form2})


def accept_usu1(request):
	users = User.objects.filter(nivelesnum__ctrl_est1__exact=True,is_active=False).order_by('id')
	
	return render(request, 'coordinator/usu_accept.html',{'users1':users})


def usu_accepted1(request,pk):
	#userap
	if request.user.is_superuser:
		usertoAc = get_object_or_404(User, pk=pk)
		usertoAc.is_active = True
		usertoAc.save()
		return redirect('accept_usu1')
	else:
		return redirect ("/")

def usu_deleted1(request, pk):
    if request.user.is_superuser:
        usertoDel = get_object_or_404(User, pk=pk)
        nombr = usertoDel.username
        usertoDel.delete()
        #messages.success(request, 'Usuario '+str(nombr)+' Eliminado exitosamente')
        return redirect('accept_usu1')

    else:
        return redirect ("/")


def carreras_list(request):
	if request.method == "POST":
	    form = form_add = carreras_add(request.POST)
	    
	    if form.is_valid():
	    	post = form.save(commit=False)
	    	post.user_edit = request.user
	    	post.date_edit = timezone.now()
	    	post.save()

	    	return redirect('carreras_list')
	else:
		carreras_q = carreras.objects.order_by('id')
		for carrera in carreras_q:
			carrera.secciones = 0
			print (carrera)
		form_add = carreras_add()
		carreras1 = []

		return render(request, 'CtrlEstud/carreras_list.html',{'users1':carreras_q,'form1':form_add})

def carrera_detal(request, pk):
	if request.method == "POST":
		form = carrera_seccion_F(request.POST)

		if form.is_valid():

			post = form.save(commit=False)
			post.carrera = carreras.objects.get(pk=pk)
			post.user_edit = request.user
			post.date_edit = timezone.now()
			post.save()
			return redirect('carrera_detal', pk=pk)
	
	else:
		carreras_q = get_object_or_404(carreras, pk=pk)
		secciones_q = carrera_seccion.objects.filter(carrera = pk).order_by('id')
		for seccion in secciones_q:
			#filter().count()
			seccion.alumnos = 0
		form = carrera_seccion_F()
		return render(request, 'CtrlEstud/carrera_detal.html', {'users1':secciones_q,'carrera': carreras_q,'form1':form})

def seccion_carrera(request, pk):
	if request.method == "POST":
		form = materia_seccion_F(request.POST)
		#username = request.POST.get('username')
		
		if form.is_valid():
			post = form.save(commit=False)
			post.seccion = carrera_seccion.objects.get(pk = pk)
			post.user_edit = request.user
			post.date_edit = timezone.now()
			post.save()
			return redirect('seccion_carrera', pk=pk)

	else:
		#carreras_q = get_object_or_404(carreras, pk=pk)
		#print(pk)
		secciones_q = carrera_seccion.objects.get(pk = pk)
		materias_q = materia_seccion.objects.filter(seccion = pk).order_by('id')

		for materia in materias_q:
			materia.alumnos = MateriasEstu.objects.filter(materia = materia.pk).order_by('id').count()
			if (MateriaTeacher.objects.filter(materia = materia.pk).exists() ):
				materia.profesor = MateriaTeacher.objects.filter(materia = materia.pk)[0].profesor

		form = materia_seccion_F()
		form2 = DatosAddF()
		#form3 = materias_listF()
		
		return render(request, 'CtrlEstud/seccion_carrera.html', {'form2':form2,'users1':materias_q,'form1':form,'seccion':secciones_q})


def verificiar_usuario(request):
    #Ajax that user exist?
    username = request.GET.get('username', None)
    usu_ex = User.objects.filter(username__exact=username).exists()
    data = {
        'usuario_tomado': usu_ex
    }
    return JsonResponse(data)

def usu_add(request, type1, pk, pk_materia):
	#User student adding
	if request.method == 'POST':
		
		form2 = DatosAddF(request.POST)

		"""
		materias_list = request.POST.getlist('choices')
		print (materias_list)
		for materia in materias_list:
			mate = materia_seccion.objects.filter(id=materia)[0]
			print(mate.materia_nom)
		"""


		#username = request.GET.get('username', None)
		username = request.POST.get('cedula', None)
		usu_ex = User.objects.filter(username__exact=username).exists()

		# requesting fields

		# if not form2, *user doesn't exist
		# then will execute else *user exist
		if form2.is_valid():
			post = form2.save(commit = False)

			#creating an user
			User.objects.create_user(username=username,password=username)
			user_to_register = User.objects.get(username=username)
			post.usuario =  user_to_register
			#user_to_register.NivelUsu.nivel_usu = nivel_estudiante
			#user_to_register.save()
			if (type1 == 1):
				NivelUsu.objects.create(user=user_to_register , nivel_usu= NivelesNum2.objects.get(pk=nivel_estudiante) )
			if (type1 == 2):
				NivelUsu.objects.create(user=user_to_register , nivel_usu= NivelesNum2.objects.get(pk=nivel_profesor) )				
			
			post.save()

			if (type1 == 1):
				#modulo de anadir materias
				materias_list = request.POST.getlist('choices')
				est_add_materia(user_to_register, materias_list)

			if (type1 == 2):
				#modulo de anadir profesor a materia
				prof_add_materia(user_to_register ,pk_materia)

			return redirect(seccion_carrera,pk=pk)
		else:
			#modulo de anadir materias
			user_to_register = User.objects.get(username=username)

			if (type1 == 1):
				#modulo de anadir materias
				materias_list = request.POST.getlist('choices')
				est_add_materia(user_to_register, materias_list)
			if (type1 == 2):
				#modulo de anadir profesor a materia
				prof_add_materia(user_to_register ,pk_materia)
				
			return redirect(seccion_carrera,pk=pk)
