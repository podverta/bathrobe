from django.shortcuts import render
from .models import Toys, Towels, Bathrobes
from django.db.models import Avg, Sum

def toys(request):
    """display all toys"""
    toys = Toys.objects.all()
    total = Toys.objects.aggregate(Sum('quantity'))
    total_price = round(Toys.objects.aggregate(Sum('price_quantity'))
                        ['price_quantity__sum'], 2)
    avg_price = round(Toys.objects.aggregate(Avg('price'))
                      ['price__avg'], 2)
    context = {'toys': toys, 'total': total.get('quantity__sum'),
               'price_all': total_price, 'avg_price': avg_price,
               }
    return render(request, 'bb/toys.html', context)

def towels(request):
    """display all towels"""
    towels = Towels.objects.all()
    total = Towels.objects.aggregate(Sum('quantity'))
    total_price = round(Towels.objects.aggregate(Sum('price_quantity'))
                        ['price_quantity__sum'], 2)
    avg_price = round(Towels.objects.aggregate(Avg('price'))
                      ['price__avg'], 2)
    context = {'towels': towels, 'total': total.get('quantity__sum'),
               'price_all': total_price, 'avg_price': avg_price,
               }
    return render(request, 'bb/towels.html', context)

def bathrobes(request):
    """display all bathrobes"""
    bathrobes = Bathrobes.objects.all()


    total = Bathrobes.objects.aggregate(Sum('quantity'))
    total_price = round(Bathrobes.objects.aggregate(Sum('price_quantity'))
                        ['price_quantity__sum'], 2)
    avg_price = round(Bathrobes.objects.aggregate(Avg('price'))
                      ['price__avg'], 2)
    context = {
        'bathrobes': bathrobes, 'total': total.get('quantity__sum'),
        'price_all': total_price, 'avg_price': avg_price,
    }

    return render(request, 'bb/bathrobes.html', context)



# Create your views here.
