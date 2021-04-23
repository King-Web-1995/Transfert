from django import forms
from django.contrib.auth.models import User
from . import models



class TransfertForm(forms.ModelForm):

    class Meta:
        model=models.Transfert
        fields=['bonguo','cbonguo']


class RetraitForm(forms.ModelForm):

    class Meta:
        model=models.Retrait
        fields=['bonguo','cbonguo']


class DepotForm(forms.ModelForm):

    class Meta:
        model=models.Depot
        fields=['bonguo','cbonguo']


class DepenseForm(forms.ModelForm):

    class Meta:
        model=models.Depense
        fields=['benun','lettre','partdeux','likambom','cpartdeux','lignebuget']

        


