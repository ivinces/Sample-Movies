from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.movies.models import Registro,Pelicula,Persona


class RegistroForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombre',
			'last_name': 'Apellido',
			'email': 'Correo',
		}


class CalificacionForm(forms.ModelForm): 	
	
	class Meta:
		model=Registro
		fields = [
			"pelicula",
			"cliente",			
			"calificacion"
		]

class UsuarioForm(forms.ModelForm): 	
	id = forms.IntegerField(widget=forms.HiddenInput())
	class Meta:
		model=Persona
		fields = [
			'id',
			"nombre",
			"apellido",			
			"ciudad",
			"paisnac",
			"tipoplan"
		]
		labels = {
			"nombre": 'Nombre',
			"apellido": 'Apellido',			
			"ciudad":'Ciudad',
			"paisnac":'País',
			"tipoplan":'Tipo de Plan',
		}

class PeliculaForm(forms.ModelForm): 	
	id = forms.IntegerField(widget=forms.HiddenInput())
	class Meta:
		model=Pelicula
		fields = [
			'id',
			"titulo",
			"director",			
			"reparto",
		]
		labels = {
			"titulo": 'Título',
			"director": 'Director',			
			"reparto":'Reparto',
		}

class CalificacionForm2(forms.ModelForm):

	cliente= forms.ModelChoiceField(queryset=Registro.objects.values_list("cliente",flat=True).distinct())
	pelicula= forms.ModelChoiceField(queryset=Registro.objects.values_list("pelicula",flat=True).distinct())
	calificacion= forms.CharField(max_length=50)

	class Meta:
		model=Registro
		fields = [
			"cliente",
			"pelicula",
			"calificacion"
		]
		model=Persona
		fields = [
			"cliente"
		]
		model=Pelicula
		fields = [
			"pelicula"
		]