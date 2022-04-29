from django.forms import ModelForm, Select, ModelChoiceField, ChoiceField, widgets, forms, IntegerField, HiddenInput, CharField
from .models import Towels, Item

class TowelsForm(ModelForm):
    type_name = ModelChoiceField(Item.objects.filter(name='Полотенце'), label='Тип товара', initial='Полотенце',)

    class Meta:
        model = Towels
        fields = [ 'type_name', 'color', 'size', 'price', 'quantity', 'comments']


