from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Registro
from .controller import ListPerson

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

	usuario= forms.ModelChoiceField(queryset=Registro.objects.values_list("cliente",flat=True).distinct())
	titulo= forms.ModelChoiceField(queryset=Registro.objects.values_list("pelicula",flat=True).distinct())
	calificacion= forms.ModelChoiceField(queryset=Registro.objects.values_list("calificacion",flat=True).distinct())

	class Meta:
		model=Registro
		fields = [
			"titulo",
			"usuario",			
			"calificacion"
		]
		

