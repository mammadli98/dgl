from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2 and password1!='' and password2!='':
            if User.objects.filter(username=username).exists() or username=='':
                messages.info(request, 'Username Taken')
                return redirect('/accounts/register')
            elif User.objects.filter(email=email).exists() or email=='':
                messages.info(request, 'Email Taken')
                return redirect('/accounts/register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                user1 = authenticate(request, username=username, password=password1)
                login(request, user1)
                return redirect('/accounts/register2')
        else:
            messages.info(request, 'Password is not match')
            return redirect('/accounts/register')
    else:    
        return render(request, 'register1.html')
    

def register2(request):
    if request.method == 'POST':
        user = request.user
        username=request.user.username
        name_der_praxis = request.POST['name_der_praxis']
        fachrichtung = request.POST['fachrichtung']
        strasse = request.POST['strasse']
        strasse_nr = request.POST['nr']
        postleitzahl = request.POST['postleitzahl']
        if name_der_praxis!='' and fachrichtung!='' and strasse!='' and strasse_nr!='' and postleitzahl!='':
            profile = UserProfile(user=user, username=username, fachrichtung=fachrichtung, postleitzahl=postleitzahl,name_der_praxis=name_der_praxis,strasse=strasse, strasse_nr = strasse_nr)
            profile.save()
 #          logout(request)
            return redirect('/homepage')
        else:
             messages.info(request, 'Empty Field')
             return redirect('/accounts/register2')
    else:    
        return render(request, 'register2.html')
    