from .models import MateriaTeacher ,MateriasEstu, materia_seccion
from django.contrib import messages

def est_add_materia(user_to_register, materias_list, request):
	for materia in materias_list:
		mate = materia_seccion.objects.filter(id=materia)[0]
		materia1 = materia_seccion.objects.get(pk=materia)
		mate_estu = MateriasEstu.objects.filter(student=user_to_register , materia=  materia1)
		# if not exists, create it
		if (not mate_estu.exists()):
			MateriasEstu.objects.create(student=user_to_register , materia=  materia1)
		else:
			messages.error(request, 'El estudiante ya {} tenia previamente inscrita la materia {} '.format(user_to_register.username, mate.materia_nom))

def prof_add_materia(user_to_register ,pk_materia):
	materiaid = materia_seccion.objects.filter(id=pk_materia)[0]
	materia = materia_seccion.objects.get(pk = pk_materia)

	mate_teacher = MateriaTeacher.objects.filter(materia = materia)
	if mate_teacher:
		mate_teacher = mate_teacher[0]
		mate_teacher.delete()
	MateriaTeacher.objects.create(materia = materia, profesor = user_to_register)