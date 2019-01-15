from .models import Pelicula,Registro, Persona

def PeliculasVistas():
	model=Pelicula.objects.raw('SELECT * FROM pelisvistas2()')
	return model

def ListadoPeliculas():
	model=Pelicula.objects.raw('SELECT * FROM listadopeliculas()')
	return model

def ListPersonas():
	model= Registro.objects.raw("SELECT usuario FROM listadopeliculas()")
	return model

def ListPeli():
	model= Registro.objects.raw("SELECT titulo FROM listadopeliculas()")
	return model
