from django.contrib.auth.forms import UserCreationForm 
from django import forms
from . models import User,Resume,Company,Job

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

class ReForm(forms.ModelForm):
	class Meta:
		model = Resume
		fields = ["ulocation","udsg","mble"]
		widgets = {
		"ulocation":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Location",
			}),
		"udsg":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Designation",
			}),
		"mble":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile Number",
			}),
		}

class UsupForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email"]
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		}

class ComForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ["cname","city","state","estdate"]
		widgets = {
		"cname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Company Name",
			}),
		"city":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"City Name",
			}),
		"state":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"State",
			}),
		"estdate":forms.TextInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		}

class JbForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ["jtitle","jreq","jsal","jexpr",'jlocation']
		widgets = {
		"jtitle":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Job Title",
			}),
		"jreq":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Job requirements",
			}),
		"jsal":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Job Salary",
			}),
		"jexpr":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Job Experience",
			}),
		"jlocation":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Job Location",
			}),
		} 