from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Pelicula,Persona

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

	titulo= forms.ModelChoiceField(queryset=Pelicula.objects.values_list("titulo",flat=True).distinct())
	usuario= forms.ModelChoiceField(queryset=Persona.objects.values_list("nombre",flat=True).distinct())
	calificacion= forms.ModelChoiceField(queryset=Pelicula.objects.values_list("calificacion",flat=True).distinct())

	class Meta:
		model=Pelicula
		fields = [
			"titulo",
			
			"calificacion"
		]
		model=Persona
		fields = [
			
			"usuario"
			
		]

