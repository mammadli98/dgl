from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("homepage/")
        else:
            messages.info(request, "invalid credentials")
            return redirect("/")
    else: 
        return render(request, "login.html")

def choose(request):
    return render(request, "choose.html")


@login_required(login_url="/")
def homepage(request):
    return render(request, "home.html")

@login_required(login_url="/")
def homepage2(request):
    return render(request, "home2.html")

@login_required(login_url="/")
def homepage3(request):
    if request.method == 'POST':
        user = request.user
        profile = UserProfile.objects.get(user = user)
        ansprechpartner = request.POST['ansprechpartner']
        mitarbeiter = request.POST['mitarbeiter']
        arzt = request.POST['arzt']
        groese_praxis = request.POST['groese_praxis']
        raume = request.POST['raume']
        if ansprechpartner!='' and mitarbeiter!='' and arzt!='' and groese_praxis!='' and raume!='':
            profile.ansprechpartner = ansprechpartner
            profile.mitarbeiter = mitarbeiter
            profile.arzt = arzt
            profile.groese_praxis = groese_praxis
            profile.raume = raume
            profile.save()
 #          logout(request)
            return redirect('/homepage4')
        else:
             messages.info(request, 'Empty Field')
             return redirect('/homepage3')
        
    else:    
        return render(request, 'home3.html')

@login_required(login_url="/")
def homepage4(request):
    if request.method == 'POST':
        user = request.user
        profile = UserProfile.objects.get(user = user)
        anmerkungen = request.POST['anmerkungen']
        if anmerkungen!='' :
            profile.anmerkungen = anmerkungen
            profile.save()
 #          logout(request)
            return redirect('/homepage5')
        else:
             messages.info(request, 'Empty Field')
             return redirect('/homepage4')
        
    else:    
        return render(request, 'home4.html')

@login_required(login_url="/")
def homepage5(request):
    return render(request, "home5.html")