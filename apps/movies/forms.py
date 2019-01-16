from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Registro


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

		

