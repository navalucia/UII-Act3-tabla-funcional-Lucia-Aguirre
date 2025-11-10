# app_gym/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_gym, name='inicio_gym'),
    # URLs para Miembros
    path('miembros/', views.ver_miembros, name='ver_miembros'),
    path('miembros/agregar/', views.agregar_miembro, name='agregar_miembro'),
    # ¡Solo una URL para actualizar ahora!
    path('miembros/actualizar/<int:pk>/', views.actualizar_miembro, name='actualizar_miembro'),
    path('miembros/borrar/<int:pk>/', views.borrar_miembro, name='borrar_miembro'),
]