from django.shortcuts import render
from .models import Customer

# Create your views here.
def sales(request):
    return render(request, 'sales.html',{})

def customers(request):
    cust_list = Customer.objects.all()
    return render(request,'customers.html',{'customers':cust_list})
