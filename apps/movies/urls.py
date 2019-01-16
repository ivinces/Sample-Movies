from django.conf.urls import url
from apps.movies.views import ListarUsuario,ListarPeliculas, edit,delete,add
urlpatterns = [
	#url(r'^listar', ListarUsuario, name="usuario_listar"),
	url(r'^listar2', ListarPeliculas, name="peliculas_listar"),
	url(r'^(?P<id>\d+)/actualizar$', edit, name='actualizar-model'),
	url(r'^(?P<id>\d+)/delete$', delete, name='borrar-model'), 
	url(r'^agregar', add, name='agregar-model'), 

] 