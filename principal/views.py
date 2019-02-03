# Create your views here.
from django.shortcuts import render, render_to_response 

from django.template.context_processors import csrf 

from principal.utility import * 

from django.contrib.auth import login as auth_login 

from django.contrib.auth import authenticate 

from django.http import HttpResponseRedirect 

from django.urls import reverse 

from .controller import ListadoPeliculas,ListadoUsuario,ListadoPeliculaUsuario,ListadoPelis,ListadoUsuarioPelicula,infoPeli,ListadoUsuarioPelicula2,infoUser,ListadoPeliculaUsuario2

from django.shortcuts import render,get_list_or_404, get_object_or_404,redirect

from apps.movies.models  import Pelicula, Registro
from apps.movies.models import Persona
from .forms import CalificacionForm, UsuarioForm, PeliculaForm

def ListarPeliculas(request):
    model=ListadoPeliculas()
    context = {'object_list':model}
    return render(request,'main/main_base.html',context)  

def infoUsuario(request, id):
    #print(id)
    ident=0
    for p in ListadoUsuario(id):
        ident=p.id
        print(p.id)
    post = get_object_or_404(Persona, id=int(ident))
    print(post,"<---------")
    
    form = UsuarioForm(instance=post)
    model=ListadoPeliculaUsuario(ident)
    context = { 'form': form, 'object_list':model}
    return render(request, 'main/infouser.html', context)

def infoPeliculaEnUsuario(request, id):
    #print(id)
    ident=0
    for p in infoPeli(id):
        ident=p.id
        print(p.id)
    post = get_object_or_404(Pelicula, id=int(ident))
    print(post,"<---------")
    
    form = PeliculaForm(instance=post)
    model=ListadoUsuarioPelicula(ident)
    context = { 'form': form, 'object_list':model}
    return render(request, 'main/infopelicula.html', context)


def infoPelicula(request, id):
    #print(id)
    ident=0
    for p in ListadoPelis(id):
        ident=p.id
        print(p.id)
    post = get_object_or_404(Pelicula, id=int(ident))
    print(post,"<---------")
    
    form = PeliculaForm(instance=post)
    model=ListadoUsuarioPelicula2(ident)
    print(model,"<...............")
    context = { 'form': form, 'object_list':model}
    return render(request, 'main/infopelicula.html', context)

def infoUsuarioEnPelicula(request,id):
    ident=0
    for p in infoUser(id):
        ident=p.id
        print(p.id)
    post = get_object_or_404(Persona, id=int(ident))
    print(post,"<---------")
    
    form = UsuarioForm(instance=post)
    model=ListadoPeliculaUsuario2(ident)
    context = { 'form': form, 'object_list':model}
    return render(request, 'main/infouser.html', context)

def main_base_view(request): 

    dictionary = dict(request=request) 

    dictionary.update(csrf(request)) 

    return render_to_response('main/main_base.html', dictionary) 

  

def login(request): 

    if request.method == 'POST': 

        username = request.POST['u'] 

        password = request.POST['p'] 

        user = authenticate(username=username, password=password) 

        if user is not None: 

            auth_login(request=request, user=user) 

            return HttpResponseRedirect(reverse('principal:main_base')) 

        else: 

            msg_to_html = custom_message('Invalid Credentials', TagType.danger) 

            dictionary = dict(request=request, messages = msg_to_html) 

            dictionary.update(csrf(request)) 

        return render_to_response('main/main_base.html', dictionary)