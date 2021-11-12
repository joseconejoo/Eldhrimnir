from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.land_page, name='landing'),
    path('login', views.login1.as_view(), name='login1'),
    path('registro', views.registros1, name='registros1'),
    path('perfil', views.perfil_redirect, name= 'perfil'),
    path('perfil/<int:pk>',views.perfil_u, name='perfil_u'),
    
    path('aceptar-usuarios', views.accept_usu1, name='accept_usu1'),
    path('User?12@#|2aprove?/<int:pk>', views.usu_accepted1, name='usu_accepted1'),
    path('User?12@#|2del?/<int:pk>', views.usu_deleted1, name='usu_deleted1'),
    path('usu_anadir', views.usu_coord_creacion, name= 'usu_coord_creacion'),
    path('usu_add_ctrl_estud', views.usu_add_ctrl_estud, name= 'usu_add_ctrl_estud'),

    path('carreras', views.carreras_list, name='carreras_list'),
    path('carrera/<int:pk>', views.carrera_detal, name='carrera_detal'),
    #to add user
    path('carrera/seccion/<int:pk>', views.seccion_carrera, name='seccion_carrera'),

    path('profesor/mis_materias', views.materias_profesor, name = 'materias_profesor'),
    path('profesor/<int:pk>/cargar_eval', views.carga_evaluaciones, name = 'carga_evaluaciones' ),

    path('api/profesor/materia_add_eval/num_eval/<int:pk_eval>', views.carga_eval, name= 'carga_eval' ),
    path('api/usuadd/<int:type1>/<int:pk>/<int:pk_materia>', views.usu_add, name='usu_add'),
    
    path('ajax/user_exist/', views.verificiar_usuario, name='verificiar_usuario'),
]