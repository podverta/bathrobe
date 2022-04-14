from django.shortcuts import render, redirect
from .models import Toys, Towels, Bathrobes
from django.db.models import Avg, Sum
from .forms import TowelsForm

def index(request):
    bathrobe_mahra = Bathrobes.objects.filter(type='Махровый')
    bathrobe_fliece= Bathrobes.objects.filter(type='Флисовый')
    towel_50_90 = Towels.objects.filter(size='50*90')
    towel_70_130 = Towels.objects.filter(size='70*130')
    toys_mi = Toys.objects.filter(toys='Зайка Ми')
    toys_jack = Toys.objects.filter(toys='Jack&Lin')
    toys_podariya = Toys.objects.filter(toys='Подария')
    toys_other = Toys.objects.filter(toys='Other')
    total_mahra = bathrobe_mahra.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_mahra = bathrobe_mahra.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_fliece = bathrobe_fliece.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_fliece = bathrobe_fliece.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_bathrobes = (total_mahra + total_fliece)
    total_price_bathrobes = total_price_mahra + total_price_fliece

    total_50_90 = towel_50_90.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_50_90 = towel_50_90.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_70_130 = towel_70_130.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_70_130 = towel_70_130.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_towels = total_50_90 + total_70_130
    total_price_towels = total_price_50_90 + total_price_70_130

    total_mi = toys_mi.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_mi = toys_mi.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_jack = toys_jack.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_jack = toys_jack.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_podariya = toys_podariya.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_podariya = toys_podariya.aggregate(
        Sum('price_quantity'))['price_quantity__sum']
    total_other = toys_other.aggregate(
        Sum('quantity'))['quantity__sum']
    total_price_other = toys_other.aggregate(
        Sum('price_quantity'))['price_quantity__sum']

    total_toys = total_mi + total_jack + total_podariya + total_other
    total_price_toys = (total_price_mi + total_price_jack
                        + total_price_podariya + total_price_other)


    context = {'total_mahra': total_mahra,
               'total_price_mahra': round(total_price_mahra, 2),
               'total_fliece': total_fliece,
               'total_price_fliece': round(total_price_fliece, 2),
               'total_bathrobes': total_bathrobes,
               'total_price_bathrobes': round(total_price_bathrobes, 2),
               'total_50_90': total_50_90,
               'total_price_50_90': round(total_price_50_90, 2),
               'total_70_130': total_70_130,
               'total_price_70_130': round(total_price_70_130, 2),
               'total_towels': total_towels,
               'total_price_towels': round(total_price_towels, 2),
               'total_mi': total_mi,
               'total_price_mi': round(total_price_mi, 2),
               'total_jack': total_jack,
               'total_price_jack': round(total_price_jack, 2),
               'total_podariya': total_podariya,
               'total_price_podariya': round(total_price_podariya, 2),
               'total_other': total_other,
               'total_price_other': round(total_price_other, 2),
               'total_toys': total_toys,
               'total_price_toys': round(total_price_toys, 2),
               }

    return render(request, 'bb/index.html', context)


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

def edit_towels(request, towels_id):
    towel= Towels.objects.get(id=towels_id)
    type = towel.type_name

    if request.method != 'POST':
        form = TowelsForm(instance=towel)
    else:
        form = TowelsForm(instance=towel, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bb:towels')
    context = {'towel': towel, 'type': type, 'form': form}
    return render(request, 'bb/edit_towels.html', context)

def new_towels(request):
    if request.method != 'POST':
        # data not was sent; creates clear form.
        form = TowelsForm()
    else:
        #sent data POST; process data.
        form = TowelsForm(data=request.POST)
        if form.is_valid():
            new_towels = form.save(commit=False, )
            new_towels.save()
            return redirect('bb:towels')
    #output an epmty or invalid form:
    context = {'form': form}
    return render(request, 'bb/new_towels.html', context)


