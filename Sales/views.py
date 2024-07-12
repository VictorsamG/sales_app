from django.shortcuts import render

# Create your views here.
def sales(request):
    return render(request, 'sales.html',{})

def customers(request):
    return render(request,'customers.html',{})
