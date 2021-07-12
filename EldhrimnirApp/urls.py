from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.login1.as_view(), name='login1'),
    path('registro', views.registros1, name='registros1'),
    path('perfil', views.perfil_redirect, name= 'perfil'),
    path('perfil/<int:pk>',views.perfil_u, name='perfil_u'),
    
    path('aceptar-usuarios', views.accept_usu1, name='accept_usu1'),
    path('User?12@#|2aprove?/<int:pk>', views.usu_accepted1, name='usu_accepted1'),
    path('User?12@#|2del?/<int:pk>', views.usu_deleted1, name='usu_deleted1'),

    path('carreras', views.carreras_list, name='carreras_list'),
    path('carrera/<int:pk>', views.carrera_detal, name='carrera_detal'),
    path('carrera/seccion/<int:pk>', views.seccion_carrera, name='seccion_carrera'),
    
]