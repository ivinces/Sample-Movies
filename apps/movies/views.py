from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView,ListView, View
from django.urls import reverse_lazy 
from apps.movies.forms import RegistroForm 
from .models import Pelicula
from django.http import HttpResponse
from .controller import PeliculasVistas, ListadoPeliculas
from .forms import CalificacionForm


def ListarUsuario(request): 
	model=PeliculasVistas()
	context = {'object_list':model}
	return render(request,'listar.html',context)

def ListarPeliculas(request):
	model=ListadoPeliculas()
	context = {'object_list':model}
	return render(request,'listar2.html',context)

class PeliculasFormView(View):
	form_class= CalificacionForm
	template_name= "actualizar.html"

	def get(self,request):
		form= self.form_class(None)
		return render(request,self.template_name,{"form":form})