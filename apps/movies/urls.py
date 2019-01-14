from django.conf.urls import url
from apps.movies.views import ListarUsuario,ListarPeliculas,PeliculasFormView

urlpatterns = [
	#url(r'^listar', ListarUsuario, name="usuario_listar"),
	url(r'^listar2', ListarPeliculas, name="peliculas_listar"),
	url(r'^actualizar', PeliculasFormView.as_view(), name="actualizar-model"),

] 