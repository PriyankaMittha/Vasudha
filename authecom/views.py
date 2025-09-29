from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse

def signup_customer(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd1  = request.POST.get('actual_password')
        pwd2  = request.POST.get('confirm_password')

        if pwd1 != pwd2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'authentication/signup_customer.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'authentication/signup_customer.html')

        user = User.objects.create_user(email, email, pwd1)
        user.save()
        messages.error(request, "Account created successfully. Please log in.")
        return redirect('signup_customer')      # ← only on success

    return render(request, 'authentication/signup_customer.html')

def handlelogin(request):
    return render(request, 'authentication/handlelogin.html')

def all_logins(request):
    return render(request, 'authentication/all_logins.html')

def handlelogout(request):
    return redirect('/authecom/login')

   

def signup_admin(request):
    return render(request, 'authentication/signup_admin.html')

def customer_login(request):
    # Logic for customer signup
    if request.method == "POST":
        return HttpResponse("Login sucessfully...")
    return render(request, 'authentication/customer_login.html')
    

def admin_login(request):
    return render(request, 'authentication/admin_login.html')




