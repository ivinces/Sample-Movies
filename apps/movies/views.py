from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView,ListView, View
from django.urls import reverse_lazy 
from apps.movies.forms import RegistroForm 
from .models import Pelicula, Registro
from django.shortcuts import render,get_list_or_404, get_object_or_404,redirect 
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

def edit(request, id): 
  post = get_object_or_404(Registro, id=id) 
  if request.method == "POST": 
    # update DB 
    form = CalificacionForm(request.POST, instance=post) 
    if form.is_valid(): 
      post = form.save(commit=False) 
      post.save() 
      return redirect('peliculas_listar') 
  else: 

    # show the form 
    form = CalificacionForm(instance=post)   

  context = { 'form': form }
  return render(request, 'actualizar.html', context) 

def delete(request, id): 

  post = get_object_or_404(Registro, id=id) 

  post.delete() 

  return redirect('peliculas_listar')