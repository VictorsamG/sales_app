from django.shortcuts import render
from .models import Product

# Create your views here.
def inventory(request):
    stocks = Product.objects.all()
    return render(request, 'inventory.html', {'inventory':stocks})