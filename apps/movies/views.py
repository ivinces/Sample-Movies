from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView,ListView 
from django.urls import reverse_lazy 
from apps.movies.forms import RegistroForm 
from .models import Pelicula
from django.http import HttpResponse


def ListarUsuario(request): 
	model=Pelicula.objects.raw('SELECT * FROM pelisvistas2()')
	context = {'object_list':model}
	return render(request,'listar.html',context)