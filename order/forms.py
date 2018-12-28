from django.forms import ModelForm
from .models import Order
from django import forms


class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


        widgets = {
             'order_temp': forms.Textarea(attrs={'class': 'form-control'}),
         }

