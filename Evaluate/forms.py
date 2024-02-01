from django import forms
from .models import *

class demoForm(forms.ModelForm):
    class Meta:
        model = demoModel
        fields = '__all__'