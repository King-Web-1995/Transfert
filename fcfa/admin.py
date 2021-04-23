from django.contrib import admin

from .models import * 

class TransfertAdmin(admin.ModelAdmin):
 	list_display = ('numer','lumbu','bonguo','cbonguo')

class RetraitAdmin(admin.ModelAdmin):
 	list_display = ('numer','lumbu','bonguo','cbonguo')

class DepotAdmin(admin.ModelAdmin):
 	list_display = ('numer','lumbu','bonguo','cbonguo')

class DepenseAdmin(admin.ModelAdmin):
 	list_display = ('numer','lumbu','benun','lettre','partdeux','likambom','cpartdeux','lignebuget')



admin.site.register(Transfert,TransfertAdmin)
admin.site.register(Retrait,RetraitAdmin)
admin.site.register(Depense,DepenseAdmin)
admin.site.register(Depot,DepotAdmin)
