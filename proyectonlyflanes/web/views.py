from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flan
# Create your views here.
def acerca_de_mi(request): #diccionario donde se envian los datos
    return render(request, 'acerca.html') #se pone {} si necesitamos ir agregando información

def resumen(request):
    return render(request, 'resumen.html',{})

def proyectos(request):
    return render(request, 'proyectos.html',{})


def contacto(request):
    return render(request, 'contact.html',{})


class MiVistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'



