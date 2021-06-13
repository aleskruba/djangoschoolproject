from django import forms
from .models import Grade
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class GradeForm(forms.ModelForm):
	class Meta:
		model = Grade
		fields = ('grades',)
		widgets = {
			'grades' : forms.TextInput(attrs={'class':'form-control'}),
			}


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']