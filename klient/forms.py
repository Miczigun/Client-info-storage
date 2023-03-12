from django import forms
from .models import Klient

class AddForm(forms.ModelForm):

    class Meta:
        model = Klient
        exclude = ['grupa']

