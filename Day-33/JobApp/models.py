from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class User(AbstractUser):
	c = [
		('0','Guest'),
		('1','Applicant'),
		('2','Recruiter'),
	]
	role_type = models.CharField(max_length=5,choices=c,default='0')
	uid = models.CharField(max_length=15)
	has_resume = models.BooleanField(default=False)
	has_company = models.BooleanField(default=False)

