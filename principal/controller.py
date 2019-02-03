from apps.movies.models import Pelicula,Registro, Persona

def ListadoPeliculas():
	model=Registro.objects.raw('SELECT * FROM listadopeliculas()')
	return model

def ListadoUsuario(id):
	model=Persona.objects.raw("SELECT * FROM listadousuarios("+str(id)+")")
	return model

def ListadoPeliculaUsuario(id):
	model=Pelicula.objects.raw("SELECT * FROM listadopeliculausuarios("+str(id)+")")
	return model

def ListadoPelis(id):
	model=Persona.objects.raw("SELECT * FROM listadopelis("+str(id)+")")
	return model

def ListadoUsuarioPelicula(id):
	model=Persona.objects.raw("SELECT * FROM listadousuariospelicula("+str(id)+")")
	return model

def ListadoUsuarioPelicula2(id):
	model=Persona.objects.raw("SELECT * FROM listadousuariospelicula2("+str(id)+")")
	return model

def infoPeli(id):
	model=Pelicula.objects.raw("SELECT * FROM movies_pelicula WHERE id="+str(id))
	return model

def infoUser(id):
	model=Pelicula.objects.raw("SELECT * FROM movies_persona WHERE id="+str(id))
	return model

def ListadoPeliculaUsuario2(id):
	model=Pelicula.objects.raw("SELECT * FROM listadopeliculausuarios2("+str(id)+")")
	return model