from django.shortcuts import render
from .models import Toys

from django.db.models import Sum

def toys(request):
    """output all toys"""
    toys = Toys.objects.all()
    #quantity = Toys.objects.get(quantity)
    #total = toys.objects.aggregate(Sum(quantity))
    context = {'toys': toys, 'quantity': quantity}
    return render(request, 'bb/toys.html', context)



# Create your views here.
