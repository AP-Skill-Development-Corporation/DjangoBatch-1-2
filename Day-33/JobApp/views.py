from django.shortcuts import render,redirect
from . forms import UsrForm

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		g = UsrForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/lgo')
	g = UsrForm()
	return render(request,'html/register.html',{'t':g})