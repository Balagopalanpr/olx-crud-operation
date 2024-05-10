from django.shortcuts import render,redirect
from .models import product
from django.views.generic import DetailView,DeleteView,UpdateView
from django.urls import  reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
     return render(request,'home.html')

# def register(request):
#     return render(request,'register.html')


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(cp==p):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return  redirect('olx:home')
        else:
            return HttpResponse("passwords are not same")
    return render(request,'register.html')
@login_required
def add(request):
    if(request.method=="POST"):
        n=request.POST['n']
        p=request.POST['p']
        y=request.POST['y']
        d=request.POST['d']
        i=request.FILES['i']
        m=product.objects.create(product_name=n,product_price=p,year_reg=y,product_desc=d,product_image=i)
        m.save()
        return home(request)
    return render(request,'add.html')
@login_required
def view(request):
    a=product.objects.all()
    return render(request,'view.html',{'a':a})

# def update(request):
#     return render(request,'update.html')

class update(UpdateView):
    model=product
    template_name='update.html'
    fields=['product_name','product_price','product_desc','year_reg','product_image',]
    success_url=reverse_lazy('olx:view')

class detail(DetailView):
    model=product
    template_name = "detail.html"
    context_object_name ="a"


def delete(request,n):
    m=product.objects.get(id=n)
    m.delete()
    return home(request)
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('olx:home')
        else:
            return HttpResponse("invalid Credentials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return user_login(request)