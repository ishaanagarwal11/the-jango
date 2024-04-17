from django import forms
from . import models

class CreatePrep(forms.ModelForm):
    class Meta:
        model = models.Prep
        fields = ['name', 'num', 'description']
