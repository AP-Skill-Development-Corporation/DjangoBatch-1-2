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

class Resume(models.Model):
	ulocation = models.CharField(max_length=100,null=True,blank=True)
	udsg = models.CharField(max_length=100,null=True,blank=True)
	mble = models.CharField(max_length=10,null=True,blank=True)
	usd = models.OneToOneField(User,on_delete=models.CASCADE)

class Company(models.Model):
	cname = models.CharField(max_length=100,null=True,blank=True)
	estdate = models.CharField(max_length=100,null=True,blank=True)
	city = models.CharField(max_length=50,null=True,blank=True)
	state = models.CharField(max_length=50,null=True,blank=True)
	usc = models.OneToOneField(User,on_delete=models.CASCADE)

class Job(models.Model):
	jtitle = models.CharField(max_length=100)
	jlocation = models.CharField(max_length=100)
	jreq = models.TextField()
	jexpr = models.IntegerField(default=1)
	jsal = models.PositiveIntegerField(default=20000)
	is_avail = models.BooleanField(default=True)
	jcrtm = models.DateTimeField(auto_now_add=True)
	usj = models.ForeignKey(User,on_delete=models.CASCADE)
	jcmp = models.ForeignKey(Company,on_delete=models.CASCADE)
	