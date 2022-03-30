from django.forms import ModelChoiceField
from django.contrib import admin


from .models import *


class TowelAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type_name':
            pass
            return ModelChoiceField(Item.objects.filter(name='Полотенце'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class ToysAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type_name':
            pass
            return ModelChoiceField(Item.objects.filter(name='Игрушка'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class BathrobeAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'type_name':
            pass
            return ModelChoiceField(Item.objects.filter(name='Халат'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Item)
admin.site.register(Toys, ToysAdmin)
admin.site.register(Towel, TowelAdmin)
admin.site.register(Bathrobe, BathrobeAdmin)