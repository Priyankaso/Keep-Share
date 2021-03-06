from django import forms
from .models import UserProfile,ToDoList 

from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=['username', 'first_name','last_name','email','password']

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=['mobile','city','profpic']

class ToDoListForm(forms.ModelForm):
	class Meta:
		model=ToDoList
		fields=['title']
