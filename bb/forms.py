from django import forms

from .models import Towels

class TowelsForm(forms.ModelForm):
    class Meta:
        model = Towels
        fields = ['type_name', 'color', 'size',
                  'quantity', 'price', 'comments', 'size',]
        widgets = {'comments': forms.Textarea(attrs={'cols': 80})}
