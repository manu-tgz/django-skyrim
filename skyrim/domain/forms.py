from dataclasses import fields
from django import forms
from skyrim.data.models import Race,Spell
from django.forms import widgets

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormPlayer(forms.Form):
    name=forms.CharField(label="Name", max_length=30,required=True)
    race_type=forms.ModelChoiceField(label="Race",queryset=Race.objects.all(), required=True)
    health_points=forms.IntegerField(label="Health Points", initial=0, min_value=0, required=True)
    known_spells=forms.ModelMultipleChoiceField(label="Known Spells", queryset=Spell.objects.all(), widget=widgets.SelectMultiple(attrs={'size':10}))
 

    
       
