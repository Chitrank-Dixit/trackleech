# Create your views here.
from django.shortcuts import render_to_response, render
from forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from blog.models import posts
from django.template import RequestContext

def home(request):
    return render_to_response('index.html',{}, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            new_user.backend='django.contrib.auth.backends.ModelBackend'
            login(request,new_user)
            # redirect, or however you may want to get to the main view
            return HttpResponseRedirect('search.html')
        else:
            form = UserForm()
        
        
    elif request.method == 'GET':
        form = UserForm(request.GET)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            new_user.backend='django.contrib.auth.backends.ModelBackend'
            login(request,new_user)
            # redirect, or however you may want to get to the main view
            return HttpResponseRedirect('search.html')
        else:
            form = UserForm()
        
    return render(request,'search.html',{'form': form})

'''
def signup(request):
    username=email=password=''
    if request.POST:
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
    return render_to_response('search.html',{'state':state, 'username': username})
'''    

def search(request):
    return render_to_response('search.html',{}, context_instance=RequestContext(request))