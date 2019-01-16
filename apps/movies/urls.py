from django.conf.urls import url
from apps.movies.views import ListarUsuario,ListarPeliculas, edit
urlpatterns = [
	#url(r'^listar', ListarUsuario, name="usuario_listar"),
	url(r'^listar2', ListarPeliculas, name="peliculas_listar"),
	url(r'^(?P<id>\d+)/actualizar$', edit, name='actualizar-model'),

] 