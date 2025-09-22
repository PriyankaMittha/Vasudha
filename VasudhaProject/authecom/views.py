from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    return render(request, 'authentication/signup.html')

def handlelogin(request):
    return render(request, 'authentication/handlelogin.html')

def all_logins(request):
    return render(request, 'authentication/all_logins.html')

def handlelogout(request):
    return redirect('/authecom/login')


