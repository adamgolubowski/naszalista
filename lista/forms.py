# -*- coding: utf-8 -*-
from django import forms
from .models import Item
from django.utils.translation import ugettext_lazy as _

class donorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(donorForm, self).__init__(*args, **kwargs)
        self.fields['donor'].required = True

    class Meta:
        model=Item
        fields=('donor',)
        labels = {
            'donor': _('Imie'),
        }
    
    pwd = forms.CharField(label='Hasło',widget=forms.PasswordInput)
   
    def clean_pwd(self):
        pwd = self.cleaned_data['pwd']
        if pwd !='adamiula':
            raise forms.ValidationError("Nieprawidłowe hasło")
        return pwd
        
    