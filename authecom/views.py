from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse

def signup_customer(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd1  = request.POST.get('actual_password')
        pwd2  = request.POST.get('confirm_password')

        if pwd1 != pwd2:
            messages.warning(request, "Passwords do not match.")
            return render(request, 'authentication/signup_customer.html')

        if User.objects.filter(username=email).exists():
            messages.warning(request, "Email already exists.")
            return render(request, 'authentication/signup_customer.html')

        user = User.objects.create_user(email, email, pwd1)
        user.save()
        messages.warning(request, "Account created successfully. Please log in.")
        return redirect('customer_login')      # ← only on success

    return render(request, 'authentication/signup_customer.html')

def handlelogin(request):
    return render(request, 'authentication/handlelogin.html')

def all_logins(request):
    return render(request, 'authentication/all_logins.html')

def handlelogout(request):
    return redirect('/authecom/login')

   

def signup_admin(request):
    # Logic for admin signup
    return HttpResponse("signup admin")

def customer_login(request):
    # Logic for customer signup
    return render(request, 'authentication/customer_login.html')
    

def login_admin(request):
    # Logic for admin signup
    pass




