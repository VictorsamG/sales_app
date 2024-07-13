from django.shortcuts import render
from .models import Product

# Create your views here.
def inventory(request):
    stocks = Product.objects.all()
    context = {'show_add_item':True}
    return render(request, 'inventory.html', {'inventory':stocks,'context':context})

def selected_item(request,pk):
    item = Product.objects.get(id=pk)
    return render(request,'item.html',{'item':item})

def add_item(request):
    return render(request,'add_item.html', {})