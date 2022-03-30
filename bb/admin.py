from django import forms
from django.contrib import admin


from .models import *



class BathrobesCategoryChoiceField(forms.ModelChoiceField):
    pass

class BathrobeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'item':
            return BathrobesCategoryChoiceField(Category.objects.filter(name='Халат'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Item)
admin.site.register(Toys)
admin.site.register(Towel)
admin.site.register(Bathrobe, BathrobeAdmin)