from django.urls import path
from . import views

urlpatterns = [
    path('inventory/',views.inventory,name='inventory'),
    path('item/<int:pk>', views.selected_item, name='item'),
    path('add-item/',views.add_item,name='add-item')
]

