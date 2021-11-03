from django.shortcuts import redirect, render, get_object_or_404

from django.utils import timezone
from .models import Post
from .form import UserRegister,UserLoginform
from django.contrib import messages
from django.contrib.auth import login,logout

from django.views.generic import ListView

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered')
            return redirect('post_list')
        else:
            messages.error(request,'errror')
    else:
        form=UserRegister()
    return render(request,'blog/register.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        form=UserLoginform(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)

            return redirect('post_list')
        else:
            messages.error(request,'errror')
            form=UserLoginform()
    else:
        form=UserLoginform()
    return render(request,'blog/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')


class Search(ListView):
    template_name='blog/search.html'
    context_object_name='posts'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search'))
    
    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        return context

    
