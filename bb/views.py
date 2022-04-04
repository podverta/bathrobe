from django.shortcuts import render
from .models import Toys, Towels, Bathrobes
from django.db.models import F, Sum

def toys(request):
    """display all toys"""
    toys = Toys.objects.all()
    total = Toys.objects.aggregate(Sum('quantity'))
    total_price = Bathrobes.objects.annotate(
        quantity_price=F('quantity') * F('price')
    ).aggregate(
        price_total=Sum('quantity_price')
    )
    context = {'toys': toys, 'total': total.get('quantity__sum'), 'price_all': total_price}
    return render(request, 'bb/toys.html', context)

def towels(request):
    """display all towels"""
    towels = Towels.objects.all()
    total = Towels.objects.aggregate(Sum('quantity'))
    context = {'towels': towels, 'total': total.get('quantity__sum')}
    return render(request, 'bb/towels.html', context)

def bathrobes(request):
    """display all bathrobes"""
    bathrobes = Bathrobes.objects.all()
    total = Bathrobes.objects.aggregate(Sum('quantity'))

    context = {'bathrobes': bathrobes, 'total': total.get('quantity__sum'),}
    return render(request, 'bb/bathrobes.html', context)



# Create your views here.
