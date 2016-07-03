# -*- coding: utf-8 -*-
from django import forms
from .models import Item
from django.utils.translation import ugettext_lazy as _

class donorForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('donor',)
        labels = {
            'donor': _('Twoje imie'),
        }
        
    #donor= forms.CharField(label='Twoje imie', max_length=100)
    