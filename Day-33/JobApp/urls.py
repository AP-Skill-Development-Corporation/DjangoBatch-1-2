from django.urls import path
from . import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path('lgo/',ad.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('lgt/',ad.LogoutView.as_view(template_name="html/logout.html"),name="lgtn"),
]