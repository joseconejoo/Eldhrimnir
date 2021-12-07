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

from .forms import eval_estudianteF, evaluacion_materiaF, actu_contra, Datos2rF, materias_listF, DatosAddF, materia_seccion_F, carrera_seccion_F, carreras_add, NivelesNumF1, DatosF, AuthenticationForm2, UserCreationForm2
from .models import permisos_bd, eval_estudiante, Tipo_Materia, evaluacion_materia, MateriaTeacher, MateriasEstu, NivelesNum2, NivelUsu, materia_seccion, carrera_seccion ,carreras, Datos1, NivelesNum

from .func1 import prof_add_materia, est_add_materia

from django.contrib.auth.models import User
from django.contrib import messages

from django.utils import timezone
from datetime import datetime, timedelta

from django.forms import formset_factory


def print_errors(request, form2):
	for error in form2.errors:
		messages.error(request,'{}'.format(form2.errors[error]) )

def check_user_level_exists(usu_ex):
	nivel_usu1x = NivelUsu.objects.filter(user = usu_ex)
	result = False
	if (nivel_usu1x.exists() or usu_ex.is_superuser ):
		result = True
	return result

def check_user_level_exists2(usu_ex):
	nivel_usu1x = NivelUsu.objects.filter(user = usu_ex)
	result = False
	if (nivel_usu1x.exists() ):
		nivel_usu1x = nivel_usu1x[0]
		if nivel_usu1x.nivel_usu.pk == nivel_profesor :
			result = False
		else:
			result = True
	if (usu_ex.is_superuser):
		result = True
	return result
teorica = Tipo_Materia.objects.filter(pk=1)[0].num_eval_min
practica = Tipo_Materia.objects.filter(pk=2)[0].num_eval_min
teoricayprac = Tipo_Materia.objects.filter(pk=3)[0].num_eval_min

global nivel_estudiante
nivel_estudiante = 3
nivel_control_estudios = 1
nivel_profesor = 4


def get_perm(pk_perm):
	return permisos_bd.objects.filter(pk= pk_perm)[0]
permiso_a_ctrl_seccion  = get_perm(1)
permiso_a_ctrl_estudiante = get_perm(2)
permiso_a_prof_evaluaciones = get_perm(3)


def get_mate_evals(pk):
	return evaluacion_materia.objects.filter(materia = pk).order_by('id')

def get_estudiantes(pk_materia):
	return User.objects.filter(materiasestu__materia= pk_materia ,nivelusu__nivel_usu = nivel_estudiante, is_active= True).order_by('id')

def land_page(request):
	return redirect('login1')

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

	user = authenticate(username=request.user.username, password=request.user.username)
	if user is not None:
		# authenticated
		usu_pass = False
		print ('worked')
	else:
		# no correct pass
		usu_pass = True
		print ('failed')



	condition2 = Datos1.objects.filter(usuario=pk).exists()
	condition3 = False

	if (condition2):
		condition3 = Datos1.objects.get(usuario=pk).residencia
	
	if (User.objects.filter(pk=pk).exists() and (condition2 and condition3) and usu_pass):
		usu1 = User.objects.get(pk=pk)
		dat1 = Datos1.objects.get(usuario=pk)
		niv1 = ''
		if NivelesNum.objects.filter(usuario=pk).exists():
			niv1 = NivelesNum.objects.get(usuario=pk)

		return render(request, 'perfil.html',{'niv1':niv1,'usu1':usu1,'dat1':dat1})
	else:
		#if (Datos1.objects.get(usuario=pk).nombre):
		# new login password nuevo login contraseña
		if (request.user.pk != pk):
			messages.error(request, 'El usuario no tiene un perfil creado. ')
			return redirect ('perfil')
		print (condition2,'\n\n')
		registred = None
		if (condition2 and not condition3):

			if (Datos1.objects.get(usuario=pk).nombre):
				registred = True

		elif(not Datos1.objects.get(usuario=pk).nombre):
			registred = False

		if request.method == "POST":
			if (registred == True):
				form2= Datos2rF(request.POST)
			elif(registred == False):
				form2= DatosF(request.POST)
			else:
				#form2 = False
				form2= DatosF()

			if (not usu_pass):
				form3 = actu_contra(request.POST)
			else:
				#form3 = False
				form3 = actu_contra()

			if form2.is_valid():
				post2 = form2.save(commit=False)
				post2.usuario = User.objects.get(pk=request.user.pk)
				if (registred == True):
					post2.save(update_fields=["residencia"])
					#new to edit info
				elif(registred == False):
					post2.save()
				#activate = True
				#messages.success(request, 'Registro Realizado exitosamente, Debe esperar la Aprobacion del Director')
			if form3.is_valid():
				usuario = get_object_or_404(User,pk=request.user.pk)

				nueva_contra = request.POST.get('password2')
				usuario.set_password(nueva_contra)

				usuario.save()


			return redirect('login1')

		else:
			if (registred == True):
				form2= Datos2rF()
			elif(registred == False):
				form2= DatosF()
			else:
				form2 = False
			if (not usu_pass):
				form3 = actu_contra()
			else:
				form3 = False
		return render(request,'registros1.html', {'form3':form3, 'form2':form2, 'residencia1' : registred})

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
	#users = User.objects.filter(nivelesnum__ctrl_est1__exact=True,is_active=False).order_by('id')
	users = User.objects.all().order_by('id')
	
	return render(request, 'Coordinator/usu_accept.html',{'users1':users})


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
	# control de estudios
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
			secciones_q = carrera_seccion.objects.filter(carrera = carrera.pk).order_by('id')
			if (secciones_q.exists()):
				carrera.secciones = secciones_q.count()	
			else:
				carrera.secciones = 0
			print (carrera)
		form_add = carreras_add()
		carreras1 = []

		permiso_a_ctrl_seccion  = get_perm(1)
		permiso_add1 = permiso_a_ctrl_seccion.estado_perm

		return render(request, 'CtrlEstud/carreras_list.html',{'permiso_add1':permiso_add1, 'users1':carreras_q,'form1':form_add})

def carrera_detal(request, pk):
	# control de estudios
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
			materias_q = materia_seccion.objects.filter(seccion = seccion.pk).order_by('id')
			#filter().count()
			if(materias_q.exists()):
				seccion.alumnos = materias_q.count()
			else:
				seccion.alumnos = 0
		form = carrera_seccion_F()

		permiso_a_ctrl_seccion  = get_perm(1)
		permiso_add1 = permiso_a_ctrl_seccion.estado_perm

		return render(request, 'CtrlEstud/carrera_detal.html', {'permiso_add1':permiso_add1, 'users1':secciones_q,'carrera': carreras_q,'form1':form})

def seccion_carrera(request, pk):
	# control de estudios

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

		permiso_a_ctrl_estudiante = get_perm(2)
		permiso_add1 = permiso_a_ctrl_estudiante.estado_perm
		
		return render(request, 'CtrlEstud/seccion_carrera.html', {'permiso_add1':permiso_add1, 'form2':form2,'users1':materias_q,'form1':form,'seccion':secciones_q})


def verificiar_usuario(request):
    #Ajax that user exist?
    username = request.GET.get('username', None)
    usu_ex = User.objects.filter(username__exact=username).exists()
    data = {
        'usuario_tomado': usu_ex
    }
    return JsonResponse(data)

def usu_add(request, type1, pk, pk_materia):
	# control de estudios
	#User student adding
	if request.method == 'POST':
		#form2 from seccion_carrera
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
		usu_ex = User.objects.filter(username__exact=username)

		if ((usu_ex.exists()) and (type1 == 2)):
			usu_ex2 = usu_ex[0]
			# check if user has another level
			user_has_level = check_user_level_exists2(usu_ex2)

			if (user_has_level):
				messages.error(request, 'El usuario {} ya tiene un nivel asignado'.format(usu_ex2.username))
				return redirect(seccion_carrera,pk=pk)


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
			post.save()

			if (type1 == 1):
				NivelUsu.objects.create(user=user_to_register , nivel_usu= NivelesNum2.objects.get(pk=nivel_estudiante) )
			if (type1 == 2):
				NivelUsu.objects.create(user=user_to_register , nivel_usu= NivelesNum2.objects.get(pk=nivel_profesor) )				
			

			if (type1 == 1):
				#modulo de anadir materias
				materias_list = request.POST.getlist('choices')
				est_add_materia(user_to_register, materias_list, request)

			if (type1 == 2):
				#modulo de anadir profesor a materia
				prof_add_materia(user_to_register ,pk_materia)

			messages.success(request, 'Cambio realizado exitosamente')
			return redirect(seccion_carrera,pk=pk)
		elif(User.objects.filter(username=username).exists()):
			#form special
			#modulo de anadir materias
			user_to_register = User.objects.get(username=username)

			if (type1 == 1):
				#modulo de anadir materias
				materias_list = request.POST.getlist('choices')
				est_add_materia(user_to_register, materias_list, request)
				#Modulo para poner nivel de usuario al de estudiante
				#POR HACER
				nivel = NivelesNum2.objects.get(pk=nivel_estudiante)
			if (type1 == 2):
				#modulo de anadir profesor a materia
				prof_add_materia(user_to_register ,pk_materia)
				#Modulo para poner nivel de usuario al de estudiante
				#por hacer
				nivel = NivelesNum2.objects.get(pk=nivel_profesor)

			#to test
			nivel_usu1x = NivelUsu.objects.filter(user = user_to_register)
			if nivel_usu1x.exists() :
				nivel_usu1x = nivel_usu1x[0]
				nivel_usu1x.nivel_usu = nivel
				nivel_usu1x.save()
			else:
				NivelUsu.objects.create(user=user_to_register , nivel_usu= nivel )

			messages.success(request, 'Cambio realizado exitosamente')
			return redirect(seccion_carrera,pk=pk)
		return redirect(seccion_carrera,pk=pk)

def usu_add_ctrl_estud(request, nivel_opci = 1):
	#coordinador
	#choose = {1:nivel_control_estudios, 2: nivel_profesor}
	#nivel_choose = choose[nivel_opci]

	if request.method == 'POST':
		# form2 from usu_coord_creacion
		form2 = DatosAddF(request.POST)
		username = request.POST.get('cedula', None)
		usu_ex = User.objects.filter(username__exact=username)

		if (usu_ex.exists() ):
			usu_ex2 = usu_ex[0]
			# check if user has another level
			user_has_level = check_user_level_exists(usu_ex2)

			if (user_has_level):
				messages.error(request, 'El usuario {} ya tiene un nivel asignado'.format(usu_ex2.username))
				return redirect(usu_add_ctrl_estud)



		# control de estudios is unique so, if a user have it remove
		usu_nivel_find = NivelUsu.objects.filter(nivel_usu= nivel_control_estudios)
		if usu_nivel_find.exists() :
			usu_nivel_find = usu_nivel_find[0]
			usu_nivel_find.delete()

		# check if errors
		nombre_usu = request.POST.get('nombre', None)
		if (nombre_usu):
			print_errors(request, form2)

		# add a user with nivel

		if form2.is_valid():
			post = form2.save(commit = False)

			#creating an user
			User.objects.create_user(username=username,password=username)
			user_to_register = User.objects.get(username=username)
			post.usuario =  user_to_register
			#user_to_register.NivelUsu.nivel_usu = nivel_estudiante
			#user_to_register.save()

			post.save()

			nivel = NivelesNum2.objects.get(pk=nivel_control_estudios)
			NivelUsu.objects.create(user=user_to_register , nivel_usu= nivel )

			messages.success(request, 'Cambio realizado exitosamente')
			return redirect(usu_add_ctrl_estud)
		elif(usu_ex.exists() ):

			#form special
			#modulo de anadir materias
			user_to_register = User.objects.get(username=username)
			# nivel a convertir
			nivel = NivelesNum2.objects.get(pk=nivel_control_estudios)
			#to test
			nivel_usu1x = NivelUsu.objects.filter(user = user_to_register)
			if nivel_usu1x.exists() :
				nivel_usu1x = nivel_usu1x[0]
				nivel_usu1x.nivel_usu = nivel
				nivel_usu1x.save()
			else:
				NivelUsu.objects.create(user=user_to_register , nivel_usu= nivel )
			messages.success(request, 'Cambio realizado exitosamente')
			return redirect(usu_add_ctrl_estud)


	return redirect(usu_coord_creacion)
def materias_profesor(request):
	# profesor
	materias_q = materia_seccion.objects.filter(materiateacher__profesor = request.user.pk).order_by('id')
	for materia in materias_q:
		materia.alumnos = MateriasEstu.objects.filter(materia = materia.pk).order_by('id').count()

	return render(request, 'Profesor/carreras_asignadas.html', {'users1': materias_q})

def carga_evaluaciones(request, pk):
	# Profesor 
	materia_actual = materia_seccion.objects.filter(pk = pk).order_by('id')[0]
	if request.method == 'POST':
		form = evaluacion_materiaF(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.materia = materia_actual

			evaluaciones_q = get_mate_evals(pk)
			total_percent = 0
			total_percent += post.ponderacion

			errors = 0
			for evaluacion in evaluaciones_q:
				total_percent += evaluacion.ponderacion
			# start validation
			materias_q = materia_actual
			estudiantes  = get_estudiantes(materias_q)
			#estudiantes = User.objects.filter(materiasestu__materia= materias_q ,nivelusu__nivel_usu = nivel_estudiante, is_active= True).order_by('id')
			form2m = formset_factory(eval_estudianteF, extra= estudiantes.count() )
			
			estu_count = 1
			estud_list = {}
			for estudiante in estudiantes:
				estud_list[estu_count] = estudiante
				estu_count += 1
				
			print(estud_list)
			
			# end form2 carga estudiantes notas
			#materias_q = materia_actual
			#messages.success(request, 'Fecha no valida.')
			min_evals = materia_actual.tipo_mate.num_eval_min
			# min_evals*5 that is min value for evaluations
			evaluaciones_q = get_mate_evals(pk)
			total_percent = 0
			total_evals = 0
			for evaluacion in evaluaciones_q:
				total_percent += evaluacion.ponderacion
				total_evals += 1

			verif1 = min_evals-total_evals
			#print (verif1)
			to_reajust = 0
			if (verif1 > 0):
				# multiply by 5 because is the minimun
				verif1 = (verif1 - 1)
				total_percent += verif1 * 5
				to_reajust = verif1 * 5

			#reajust total_percent to print
			materias_q.total_percent = total_percent - to_reajust

			if (total_percent < 70):
				max_value = 30
			else:
				max_value = (-total_percent) + 100

			# end validation nota
			if (total_percent > 100 ):
				messages.error(request, 'Porcentaje total no puede ser mayor al 100 %')
				print('not allowed')
				errors += 1
			hoy_o_anterior = (datetime.now() + timedelta(1)).date()
			if (post.fecha < hoy_o_anterior):
				messages.error(request, 'La fecha de la evaluacion no puede ser hoy, ni anterior a hoy')
				errors += 1
			if ( errors == 0):
				post.save()
				messages.success(request, 'Evaluación registrada')

			return redirect('carga_evaluaciones', pk=pk)

	else:
		form = evaluacion_materiaF()
		# form2 carga estudiantes notas
		materias_q = materia_actual
		estudiantes  = get_estudiantes(materias_q)
		#estudiantes = User.objects.filter(materiasestu__materia= materias_q ,nivelusu__nivel_usu = nivel_estudiante, is_active= True).order_by('id')
		form2m = formset_factory(eval_estudianteF, extra= estudiantes.count() )
		
		estu_count = 1
		estud_list = {}
		for estudiante in estudiantes:
			estud_list[estu_count] = estudiante
			estu_count += 1
			
		print(estud_list)
		
		# end form2 carga estudiantes notas
		#materias_q = materia_actual
		#messages.success(request, 'Fecha no valida.')
		min_evals = materia_actual.tipo_mate.num_eval_min
		# min_evals*5 that is min value for evaluations
		evaluaciones_q = get_mate_evals(pk)
		total_percent = 0
		total_evals = 0
		for evaluacion in evaluaciones_q:
			total_percent += evaluacion.ponderacion
			total_evals += 1

		verif1 = min_evals-total_evals
		#print (verif1)
		to_reajust = 0
		if (verif1 > 0):
			# multiply by 5 because is the minimun
			verif1 = (verif1 - 1)
			total_percent += verif1 * 5
			to_reajust = verif1 * 5

		#reajust total_percent to print
		materias_q.total_percent = total_percent - to_reajust

		if (total_percent < 70):
			max_value = 30
		else:
			max_value = (-total_percent) + 100


		date_min_value = timezone.now() + timedelta(1)
		date_min_value = str(date_min_value.day) +'/'+ str(date_min_value.month)+'/'+ str(date_min_value.year)
		#print(date_min_value)
		allow_anadir_eval = True
		if (materias_q.total_percent == 100):
			allow_anadir_eval = False


		#cargar notas
		for eval1 in evaluaciones_q:
			ahoramismo = (datetime.now() + timedelta(0)).date()
			#ahoramismo = (timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)).date()
			#5 dias habiles para cargar notas
			limite = eval1.fecha + timedelta(5)
			#print(ahoramismo, '\n', limite)
			eval1.permiso_cargar = False
			eval1.tooltip_title = 'Se podra cargar el {} y 5 dias posteriores'.format(eval1.fecha)
			if ((ahoramismo >= eval1.fecha) and (ahoramismo <= limite) ):
				eval1.permiso_cargar = True			
			cargar_fuera_tiempo = get_perm(3)
			if (cargar_fuera_tiempo.estado_perm):
				eval1.permiso_cargar = True
			check_if_eval_has_evaluated = eval_estudiante.objects.filter(evaluacion_num = eval1.pk)
			#if (eval1.permiso_cargar and check_if_eval_has_evaluated.exists() ):
			if (check_if_eval_has_evaluated.exists() ):
				eval1.permiso_cargar = False
				eval1.cargada = True
				eval1.tooltip_title = 'Ya se han cargado notas en esta evaluación '


		#Ver notas cargadas
		ver_notas_lista = False
		if (total_percent == 100):
			ver_notas_lista = True

		per_notas_ver = False
		if (request.user.nivelusu.nivel_usu.pk in [nivel_control_estudios, nivel_profesor] ):
			per_notas_ver = True



		return render(request, 'Profesor/carga_evaluaciones.html', {'per_notas_ver':per_notas_ver, 'ver_notas_lista':ver_notas_lista, 'estud_list':estud_list, 'form2m':form2m, 'allow_anadir_eval':allow_anadir_eval, 'date_min_value':date_min_value, 'max_value':max_value, 'evaluaciones': evaluaciones_q, 'materia': materias_q,'form1': form})
def carga_eval(request, pk_eval, pk_materia):
	# profesor
	evaluaciones_q2 = evaluacion_materia.objects.filter(pk= pk_eval,materia = pk_materia).order_by('id')

	if (evaluaciones_q2.exists()):
		evaluaciones_q2 = evaluaciones_q2[0]

	
	estudiantes  = get_estudiantes(pk_materia)
	
	form2m = formset_factory(eval_estudianteF, extra= estudiantes.count() )
	formset_1 = form2m(data=request.POST)

	if (formset_1.is_valid()):
		estud_count = 0
		#detail_instances = formset_1.save(commit=False)

		for f in formset_1.forms:
			
			

			#f.cleaned_data['student'] = estudiantes[estud_count]
			#f.cleaned_data['evaluacion_num'] = evaluaciones_q2.pk

			evaluacion_estud_q = eval_estudiante.objects.filter(student= estudiantes[estud_count], evaluacion_num= evaluaciones_q2.pk)
			nota_x = f.cleaned_data['nota']
			asistente_x = f.cleaned_data['asistente']

			if (not evaluacion_estud_q.exists()):
				eval_estudiante.objects.create(student= estudiantes[estud_count],
					 evaluacion_num= evaluaciones_q2,
					  nota= nota_x,
					  asistente= asistente_x )

			else:
				evaluacion_estud_q = evaluacion_estud_q[0]
				#evaluacion_estud_q.student = estudiantes[estud_count]
				#evaluacion_estud_q.evaluacion_num = evaluaciones_q2.pk
				evaluacion_estud_q.nota = nota_x
				evaluacion_estud_q.asistente = asistente_x
				evaluacion_estud_q.save()
			#f['student'] = estudiantes[estud_count]
			#f['evaluacion_num'] = evaluaciones_q2.pk
			# hacer filtrado a ver si existe la evaluacion para el estudiante
			# si no existe crearla, si existe actualizar los valores como d_amazon

			"""
			to_save = eval_estudianteF()
			to_save.student = estudiantes[estud_count]
			to_save.evaluacion_num_id = evaluaciones_q2.pk
			to_save.nota = f.cleaned_data['nota']
			to_save.asistente = f.cleaned_data['asistente']
			to_save.save()
			f.save()
			"""
			
			estud_count += 1
			

	return redirect('carga_evaluaciones', pk = evaluaciones_q2.materia.pk)

def vista_evals(request, pk_materia):
	# profesor
	materia_actual = materia_seccion.objects.filter(pk = pk_materia).order_by('id')[0]
	materias_q = materia_actual

	evaluaciones_q = get_mate_evals(pk_materia)
	estudiantes  = get_estudiantes(pk_materia)

	evals_estud_all = {}
	for estudiante in estudiantes:
		#evaluacion_estud_q_all = eval_estudiante.objects.filter(student= estudiante.pk, evaluacion_num__in= evaluaciones_q)
		
		evals_estud = []
		total_notas = 0
		total_asistencias = 0
		#x_evalcount = (evaluaciones_q.count()) - (evaluacion_estud_q_all.count())
		for evaluacion in evaluaciones_q:
			evals = eval_estudiante.objects.filter(student= estudiante.pk, evaluacion_num= evaluacion.pk)
			if (evals):
				# append nota
				evals = evals[0]
				#evals_estud.append([evals.nota,evals.asistente])
				total_notas += evals.nota
				if (evals.asistente):
					total_asistencias += 1
				evals_estud.append(evals.nota)
			else:
				# append nothing
				evals_estud.append('')
				pass

			
		"""
		for x in range(x_evalcount):
			evals_estud.append('')
		"""
		if (evaluaciones_q.count() > 0):
			estudiante.asistencia = (total_asistencias/evaluaciones_q.count())*100
			estudiante.asistencia = float("{:.2f}".format(estudiante.asistencia) )
		else:
			estudiante.asistencia = 0
		estudiante.notastotal20 = (total_notas*20)/100
		estudiante.notas100 = total_notas
		# working print this last three values in html 
		evals_estud_all[estudiante.pk] = evals_estud

	
	return render(request, 'Profesor/lista_notas.html', {'evals_estud_all':evals_estud_all, 'users1':estudiantes, 'evaluaciones_q':evaluaciones_q, 'materia':materias_q})

def ver_materias(request):
	# estudiante
	materias_q = materia_seccion.objects.filter(materiasestu__student = request.user.pk).order_by('id')
	for materia in materias_q:
		materia.alumnos = MateriasEstu.objects.filter(materia = materia.pk).order_by('id').count()

	titulo = 'Mis materias'
	return render(request, 'Profesor/carreras_asignadas.html', {'titulo':titulo, 'users1': materias_q})

def vista_materias_evals_estud(request, pk_estud):
	# estudiante notas
	materias_q = MateriasEstu.objects.filter(student= pk_estud)
	

	evals_estud_all = {}

	for materia in materias_q:
		evaluaciones_q = get_mate_evals(materia.materia.pk)

		evals_estud = []
		total_notas = 0
		total_asistencias = 0
		for evaluacion in evaluaciones_q:
			evals = eval_estudiante.objects.filter(student= pk_estud, evaluacion_num= evaluacion.pk)
			if (evals):
				# append nota
				evals = evals[0]
				#evals_estud.append([evals.nota,evals.asistente])
				total_notas += evals.nota
				if (evals.asistente):
					total_asistencias += 1
				evals_estud.append(evals.nota)
			else:
				# append nothing
				evals_estud.append('')
				pass

			
		"""
		for x in range(x_evalcount):
			evals_estud.append('')
		"""
		if (evaluaciones_q.count() > 0):
			materia.asistencia = (total_asistencias/evaluaciones_q.count())*100
		else:
			materia.asistencia = 0
		materia.notastotal20 = (total_notas*20)/100
		materia.notas100 = total_notas
		# working print this last three values in html 
		evals_estud_all[materia.pk] = evals_estud



	usuario_q = User.objects.get(pk = pk_estud )
	
	#EstudianteT/lista_notas2.html
	return render(request, 'EstudianteT/lista_notas2.html', {'usuario_q':usuario_q,'evals_estud_all':evals_estud_all, 'users1':materias_q, 'evaluaciones_q':evaluaciones_q, 'materia':materias_q})


def lista2_estud_materias_detal(request, pk_materia):
	#users = User.objects.all().order_by('id')
	materias_q = materia_seccion.objects.filter(pk= pk_materia)
	if (materias_q):
		materias_q = materias_q[0]
	users = User.objects.filter(materiasestu__materia= pk_materia)

	titulo = 'Lista de estudiantes'
	estud_list_mate = True
	
	return render(request, 'Coordinator/usu_accept.html',{'estud_list_mate':estud_list_mate, 'titulo':titulo, 'materias_q':materias_q, 'users1':users})
def lista3_estud_list(request):
	#users = User.objects.all().order_by('id')
	materias_q = materia_seccion.objects.filter(materiateacher__profesor= request.user.pk)
	for materia in materias_q:
		users = User.objects.filter(materiasestu__materia= materia)

		if (users):
			users = users | users

	titulo = 'Lista de todos mis estudiantes'
	
	return render(request, 'Coordinator/usu_accept.html',{'titulo':titulo, 'users1':users})
def lista4_estud_list(request):
	#users = User.objects.all().order_by('id')
	users = User.objects.filter(nivelusu__nivel_usu= nivel_profesor )

	titulo = 'Lista de todos los profesores'
	
	return render(request, 'Coordinator/usu_accept.html',{'titulo':titulo, 'users1':users})
def lista5_estud_list(request):
	#users = User.objects.all().order_by('id')
	users = User.objects.filter(nivelusu__nivel_usu= nivel_estudiante )

	titulo = 'Lista de todos los estudiantes'
	
	return render(request, 'Coordinator/usu_accept.html',{'titulo':titulo, 'users1':users})
def lista6_permisos(request):
	#coordinador
	users = permisos_bd.objects.all()
	titulo = 'Lista de permisos y Cambio de periodo'

	return render(request, 'Coordinator/usu_accept_2.html',{'titulo':titulo, 'users1':users})
def periodo_cambio(request):
	secciones = carrera_seccion.objects.all()
	if (secciones):
		secciones.delete()
	"""
	for seccion in secciones:
		seccion.delete()
	"""
	search = [nivel_estudiante, nivel_profesor]
	usuarios_nivel = NivelUsu.objects.filter(nivel_usu__in= search)
	if (usuarios_nivel):
		usuarios_nivel.delete()
	messages.success(request, 'Cambio realizado exitosamente')
	return redirect('lista6_permisos')

def perm_switch(request, pk_perm):
	#coordinador
	permission = get_perm(pk_perm)
	permission.estado_perm = not (permission.estado_perm)
	permission.save()

	messages.success(request, 'El permiso a cambiado exitosamente')

	return redirect ('lista6_permisos')
def usu_coord_creacion(request):
	# coordinador
	for x in range(1):
		ctrl_stud  = User.objects.filter(nivelusu__nivel_usu = nivel_control_estudios, is_active= True)
		cargo = NivelesNum2.objects.get(pk = nivel_control_estudios)
		print (ctrl_stud)
		if (not ctrl_stud.exists()):
			ctrl_stud = [{'cargo1':cargo.nom_nivel,'materia_nom':'','asd':'asd'}]
		else:
			for user in ctrl_stud:
				user.cargo1 = cargo.nom_nivel
				#user.cambiar = True


	form2 = DatosAddF()	
	return render(request, 'Coordinator/anadir_usu.html', {'users1' : ctrl_stud, 'form2':form2 })

