import re
from django.contrib.auth import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.urls.conf import path
from django.utils import timezone
import blog
from .models import *
from django.contrib.auth import login , logout

from .form import UserRegister,Userloginform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
def void(request):
    return render(request,'blog/about_us.html',{})
def part(request):
    parts=Parts.objects.all()
    return render(request, 'blog/part.html',{'parts':parts})
def index(request):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blog/index.html', {'posts': posts})

def bike1(request):
    bikes=Bike.objects.filter(type__contains='mountain')
    return render(request,'blog/bike1.html',{'bikes':bikes} )

def bike2(request):
    bikes=Bike.objects.filter(type__contains='kids')
    return render(request,'blog/bike2.html',{'bikes':bikes} )


def bike3(request):
    bikes=Bike.objects.filter(type__contains='speed')
    return render(request,'blog/bike3.html',{'bikes':bikes} )

def bike4(request):
    bikes=Bike.objects.filter(type__contains='bmx')
    return render(request,'blog/bike4.html',{'bikes':bikes} )
def part1(request):
    parts=Parts.objects.filter(name__icontains='wheel')
    return render(request,'blog/part1.html',{'parts':parts})

def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    return render(request, 'blog/bike_detail.html', {'bike': bike})

def part_detail(request, pk):
    part = get_object_or_404(Parts, pk=pk)
    return render(request, 'blog/part_detail.html', {'part': part})
    
def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method=='POST':
        form=Userloginform(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            
            # messages.success(request,'Registered successufuly')
            return redirect('index')
        else:
            form=Userloginform()

    else:
        form = Userloginform()
    return render(request,'blog/login.html',{"form":form})


def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered successufuly')
            return redirect('login')
        else:
            messages.error(request,'Error')
    else:
        form = UserRegister()
     
    return render(request, 'blog/register.html',{'form':form})





class Search(ListView):
    template_name='blog/search.html'
    context_object_name='bikes'

    def get_queryset(self):
        return Bike.objects.filter(name__icontains=self.request.GET.get('search'))

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class Sort(ListView):
    template_name='blog/sort.html'
    context_object_name='bikes'

    def get_queryset(self):
        if self.request.GET.get('priceasc')=='Sort by price asc':
            return Bike.objects.order_by('price')
        elif self.request.GET.get('pricedesc')=='Sort by price desc':
            return Bike.objects.order_by('-price')
        else:
             return Bike.objects.order_by('country')
        

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        return context















