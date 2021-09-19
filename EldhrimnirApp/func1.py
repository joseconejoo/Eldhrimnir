from .models import MateriasEstu, materia_seccion

def est_add_materia(user_to_register, materias_list):
	for materia in materias_list:
		mate = materia_seccion.objects.filter(id=materia)[0]
		MateriasEstu.objects.create(student=user_to_register , materia= materia_seccion.objects.get(pk=materia) )