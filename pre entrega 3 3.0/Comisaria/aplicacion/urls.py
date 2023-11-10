from django.urls import path
from . import views

urlpatterns = [
    path("comisarias/", views.mostrar_comisarias, name="mostrar_comisarias"),
    path("policias/", views.mostrar_policias, name="mostrar_policias"),
    path("detenidos/", views.mostrar_detenidos, name="mostrar_detenidos"),
    path("crear-comisaria/", views.crear_comisaria, name="crear-comisaria"),
    path("crear-policia/", views.crear_policia, name="crear-policia"),
    path("crear-detenido/", views.crear_detenido, name="crear-detenido"),
    path("buscar-comisaria/", views.buscar_comisaria, name="buscar-comisaria")
]
