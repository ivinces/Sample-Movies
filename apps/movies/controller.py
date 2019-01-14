from .models import Pelicula

def PeliculasVistas():
	model=Pelicula.objects.raw('SELECT * FROM pelisvistas2()')
	return model