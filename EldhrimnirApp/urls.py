from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.land_page, name='landing'),
    path('login', views.login1.as_view(), name='login1'),
    path('registro', views.registros1, name='registros1'),
    path('perfil', views.perfil_redirect, name= 'perfil'),
    path('perfil/<int:pk>',views.perfil_u, name='perfil_u'),
    
    #path('aceptar-usuarios', views.accept_usu1, name='accept_usu1'),
    path('lista-usuarios', views.accept_usu1, name='accept_usu1'),
    path('User?12@#|2aprove?/<int:pk>', views.usu_accepted1, name='usu_accepted1'),
    path('User?12@#|2del?/<int:pk>', views.usu_deleted1, name='usu_deleted1'),
    path('usu_anadir', views.usu_coord_creacion, name= 'usu_coord_creacion'),
    path('usu_add_ctrl_estud', views.usu_add_ctrl_estud, name= 'usu_add_ctrl_estud'),

    path('carreras', views.carreras_list, name='carreras_list'),
    path('carrera/<int:pk>', views.carrera_detal, name='carrera_detal'),
    #to add user
    path('carrera/seccion/<int:pk>', views.seccion_carrera, name='seccion_carrera'),

    

    path('profesor/mis_materias', views.materias_profesor, name = 'materias_profesor'),
    path('profesor/<int:pk>/cargar_eval/', views.carga_evaluaciones, name = 'carga_evaluaciones' ),
    path('profesor/<int:pk_materia>/vista_evals', views.vista_evals, name = 'vista_evals' ),

    path('estudiante/<int:pk_estud>/vista_evals', views.vista_materias_evals_estud, name = 'vista_materias_evals_estud' ),
    path('estudiante/mis_materias', views.ver_materias, name = 'ver_materias' ),

    path('lista/estudiantes/<int:pk_materia>', views.lista2_estud_materias_detal, name = 'lista2_estud_materias_detal' ),
    path('lista/mis/estudiantes', views.lista3_estud_list, name = 'lista3_estud_list' ),
    path('lista/todos_los/profesores', views.lista4_estud_list, name = 'lista4_estud_list' ),
    path('lista/todos_los/estudiantes', views.lista5_estud_list, name = 'lista5_estud_list' ),
    path('lista/todos_los/permisos', views.lista6_permisos, name = 'lista6_permisos' ),
    
    path('api/profesor/materia_add_eval/num_eval/<int:pk_eval>/<int:pk_materia>/materia', views.carga_eval, name= 'carga_eval' ),
    path('api/usuadd/<int:type1>/<int:pk>/<int:pk_materia>', views.usu_add, name='usu_add'),
    path('api/perm_switch/<int:pk_perm>', views.perm_switch, name='perm_switch'),
    path('api/periodo_cambio', views.periodo_cambio, name='periodo_cambio'),
    
    
    path('ajax/user_exist/', views.verificiar_usuario, name='verificiar_usuario'),
]