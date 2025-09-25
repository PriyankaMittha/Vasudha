from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def signup(request):
    return render(request, 'authentication/signup.html')

def handlelogin(request):
    return render(request, 'authentication/handlelogin.html')

def all_logins(request):
    return render(request, 'authentication/all_logins.html')

def handlelogout(request):
    return redirect('/authecom/login')

def signup_customer(request):
    # Logic for customer signup
    return HttpResponse("signup customer")
    

def signup_admin(request):
    # Logic for admin signup
    return HttpResponse("signup admin")

def login_customer(request):
    # Logic for customer signup
    pass

def login_admin(request):
    # Logic for admin signup
    pass




