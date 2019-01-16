from django.conf.urls import url
from apps.movies.views import ListarUsuario,ListarPeliculas, edit,delete
urlpatterns = [
	#url(r'^listar', ListarUsuario, name="usuario_listar"),
	url(r'^listar2', ListarPeliculas, name="peliculas_listar"),
	url(r'^(?P<id>\d+)/actualizar$', edit, name='actualizar-model'),
	url(r'^(?P<id>\d+)/delete$', delete, name='borrar-model'), 

] 