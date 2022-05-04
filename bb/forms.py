from django.forms import ModelForm, ModelChoiceField
from .models import Towels, Item

class TowelsForm(ModelForm):
    type_name = ModelChoiceField(Item.objects.filter(name='Полотенца'),
                                 label='Тип товара', initial='Полотенца',)

    class Meta:
        model = Towels
        fields = ['type_name', 'color', 'size',
                   'price', 'quantity', 'comments']


