from django.conf.urls import url
from apps.movies.views import ListarUsuario

urlpatterns = [
	url(r'^listar', ListarUsuario, name="usuario_listar"),
] 