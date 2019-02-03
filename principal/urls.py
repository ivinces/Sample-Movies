from django.conf.urls import url 

from . import views  

app_name = 'principal'  

urlpatterns = [  

    url(r'^$', views.main_base_view, name='main_base'), 

    url(r'^login/$', views.login, name='login'),  

    url(r'^lp/$', views.ListarPeliculas, name="peliculas_listar"),

    url(r'^(?P<id>\d+)/infousuario/$', views.infoUsuario, name='infousuario-model'),

    url(r'^(?P<id>\d+)/infopelicula/$', views.infoPeliculaEnUsuario, name='infopelicula-model'),

    url(r'^(?P<id>\d+)/infopeliculas/$', views.infoPelicula, name='infopelis-model'),

    url(r'^(?P<id>\d+)/infousuarios/$', views.infoUsuarioEnPelicula, name='infousers-model'),

]