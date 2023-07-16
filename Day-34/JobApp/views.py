from django.shortcuts import render,redirect
from . forms import UsrForm,ReForm,UsupForm,ComForm,JbForm
from . models import User,Job,Company

# Create your views here.

def home(request):
	k = Job.objects.filter(usj_id=request.user.id)
	f = Job.objects.all()
	c = Company.objects.all()
	cdt,jct = {},{}
	for i in c:
		cdt[i.id] = i.cname
	for j in f:
		if j.jcmp_id in cdt:
			jct[j.id]=j.jtitle,j.jreq,j.jlocation,j.jsal,j.jcrtm,j.jexpr,cdt[j.jcmp_id]
	return render(request,'html/home.html',{'rj':k,'uj':jct.values()})

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

def resumecr(request):
	w = User.objects.get(id=request.user.id)
	if request.method == "POST":
		t = ReForm(request.POST)
		y = UsupForm(request.POST,instance=w)
		if t.is_valid() and y.is_valid():
			k = t.save(commit=False)
			k.usd_id = request.user.id
			w.has_resume = 1
			w.save()
			y.save()
			k.save()
			return redirect('/')
	t = ReForm()
	y = UsupForm(instance=w)
	return render(request,'html/resumecrt.html',{'q':y,'r':t})

def cmpnycr(request):
	v = User.objects.get(id=request.user.id)
	if request.method=="POST":
		h = ComForm(request.POST)
		if h.is_valid():
			w = h.save(commit=False)
			w.usc_id = request.user.id
			v.has_company = 1
			w.save()
			v.save()
			return redirect('/')
	h = ComForm()
	return render(request,'html/crcompany.html',{'b':h})

def jbcrt(request):
	h = Job.objects.filter(usj_id=request.user.id)
	if request.method == "POST":
		t = JbForm(request.POST)
		if t.is_valid():
			c = t.save(commit=False)
			c.usj_id = request.user.id
			c.jcmp_id = request.user.company.id
			c.save()
			return redirect('/jblst')
	t = JbForm()
	return render(request,'html/jblist.html',{'w':t,'s':h})








