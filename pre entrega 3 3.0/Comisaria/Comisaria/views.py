from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response