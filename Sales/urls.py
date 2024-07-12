from django.urls import path
from . import views

urlpatterns = [
    path('sales/', views.sales, name='sales'),
    path('customers/',views.customers, name ='customers')
]
