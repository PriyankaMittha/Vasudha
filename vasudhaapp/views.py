from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ecom/index.html')

def contact(request):
    return render(request, 'ecom/contact.html')

def about(request):
    return render(request, 'ecom/about.html')