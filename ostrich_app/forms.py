from django import forms
from .models import OstrichBreeders


class AddBreederForm(forms.ModelForm):
    class Meta:
        model = OstrichBreeders
        fields = ['name', 'birth_year', 'sex', 'description']
