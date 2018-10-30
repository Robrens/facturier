from django import forms
from .models import Client, Product, Ligne, QuoteBill, status


class QuotationFormLine(forms.ModelForm):
    
    class Meta:
        model = Ligne
        fields = "__all__"
