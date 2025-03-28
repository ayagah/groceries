from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def products(request):
    product=Product.objects.all()
    return render(request,'products.html',{'product':product})