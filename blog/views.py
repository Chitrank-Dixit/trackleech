# Create your views here.
from django.shortcuts import render_to_response, render
from forms import UserForm , SignedUserForm
from django.contrib import auth
from django.contrib.auth import login , logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
# sending mail usin Django
from django.core.mail import send_mail

def home(request):
    return render_to_response('index.html',{}, context_instance=RequestContext(request))

def signup(request):
    send_email=''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            new_user.backend='django.contrib.auth.backends.ModelBackend'
            login(request,new_user)
            send_email=request.POST.get('email')
            # redirect, or however you may want to get to the main view
            return HttpResponseRedirect('index.html')
        else:
            form = UserForm()
        
        
    elif request.method == 'GET':
        form = UserForm(request.GET)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.save()
            new_user.backend='django.contrib.auth.backends.ModelBackend'
            login(request,new_user)
            send_email=request.GET.get('email')
            # redirect, or however you may want to get to the main view
            return HttpResponseRedirect('index.html')
        else:
            form = UserForm()
    #send_mail('Subject here', 'Here is the message.', 'chitrankdixit@gmail.com',
    #[send_email], fail_silently=False)    
    return render(request,'index.html',{'form':form})


def signin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/blog/home')
    elif user is None:
        return HttpResponseRedirect('/blog/search')
        
        
    
    
    
def signout(request):
    logout(request)
    return render_to_response('index.html',{}, context_instance=RequestContext(request))
 

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


def authorize(request):
    if not request.user.is_authenticated():
        return render_to_response('index.html', {'inhalt': 'Not loggged in'},context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', {'inhalt': 'Succesfully loged in'},context_instance=RequestContext(request))

def search(request):
    return render_to_response('search.html',{}, context_instance=RequestContext(request))
    
def profile(request):
    return render_to_response('profile.html',{}, context_instance=RequestContext(request))