from django.contrib.auth.forms import UserCreationForm 
from django import forms
from . models import User

class UsrForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","uid"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"uid":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Unique Id",
			}),
		}


