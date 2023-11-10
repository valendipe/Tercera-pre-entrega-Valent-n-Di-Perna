from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from aplicacion.models import Comisaria, Policia, Detenido
from aplicacion.forms import ComisariaInsertar, PoliciaInsertar, DetenidoInsertar

# Create your views here.
def mostrar_comisarias(request):
   contexto= { 
              "comisarias": Comisaria.objects.all()
   }
   http_response= render(
      request=request,
      template_name='aplicacion/mostrar_comisarias.html',
      context=contexto,
   )
   return http_response



def mostrar_policias(request):
   contexto= { 
              "policias": Policia.objects.all()
   }
   http_response= render(
      request=request,
        template_name='aplicacion/mostrar_policias.html',
        context=contexto,
   )
   return http_response

def mostrar_detenidos(request):
   contexto= { 
              "detenidos": Detenido.objects.all()
   }
   http_response= render(
      request=request,
        template_name='aplicacion/mostrar_detenidos.html',
        context=contexto,
   )
   return http_response

def crear_comisaria(request):
   if request.method == "POST":
       formulario = ComisariaInsertar(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           nombre = data["nombre"]
           numero = data["numero"]
           comisaria = Comisaria(nombre=nombre, numero=numero)  # lo crean solo en RAM
           comisaria.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('mostrar_comisarias')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = ComisariaInsertar()
   http_response = render(
       request=request,
       template_name='aplicacion/formulario_comisaria.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_policia(request):
   if request.method == "POST":
       formulario = PoliciaInsertar(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           apellido = data["apellido"]
           nombre = data["nombre"]
           telefono = data["telefono"]
           policia = Policia(apellido=apellido, nombre=nombre, telefono=telefono)  # lo crean solo en RAM
           policia.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('mostrar_policias')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = PoliciaInsertar()
   http_response = render(
       request=request,
       template_name='aplicacion/formulario_policia.html',
       context={'formulario': formulario}
   )
   return http_response

def crear_detenido(request):
   if request.method == "POST":
       formulario = DetenidoInsertar(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           apellido = data["apellido"]
           nombre = data["nombre"]
           motivo_de_detencion = data["motivo_de_detencion"]
           detenido = Detenido(apellido=apellido, nombre=nombre, motivo_de_detencion=motivo_de_detencion)  # lo crean solo en RAM
           detenido.save()  # Lo guardan en la Base de datos

           
           url_exitosa = reverse('mostrar_detenidos')
           return redirect(url_exitosa)
   else:  # GET
       formulario = DetenidoInsertar()
   http_response = render(
       request=request,
       template_name='aplicacion/formulario_detenido.html',
       context={'formulario': formulario}
   )
   return http_response

def buscar_comisaria(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        comisaria = Comisaria.objects.filter(
            Q(nombre__icontains=busqueda) | Q(numero__contains=busqueda)
        )
        contexto = {
            "comisaria": comisaria,
        }
        http_response = render(
            request=request,
            template_name='aplicacion/mostrar_comisarias.html',
            context=contexto,
        )
        return http_response