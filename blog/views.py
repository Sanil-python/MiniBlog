from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all()
        return render(request, 'blog/dashboard.html', {'blogs':blogs})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'congratulations !! You have become an Author.')
            form.save()
    else:        
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:            
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
def addblog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Blog(title=title, desc=desc)
                pst.save()
                form = BlogForm()
        else:
            form  =BlogForm()
        return render(request, 'blog/addblog.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

def updateblog(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blog.objects.get(pk=id)
            form = BlogForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Blog.objects.get(pk=id)
            form = BlogForm(instance=pi)
        return render(request, 'blog/addblog.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
def deleteblog(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Blog.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')