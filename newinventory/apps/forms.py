from .models import *
from django import forms
from django.forms import ModelForm

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = '__all__'

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = '__all__'

