from django.forms import ModelForm
from .models import Order
from django import forms


class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_temp', 'tirag', 'total_price']


        widgets = {
             'date': forms.DateTimeInput (attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'performer': forms.Select(attrs={'class': 'form-control'}),
            'total_price': forms.TextInput(attrs={'class': 'form-control'}),
            'discount': forms.TextInput(attrs={'class': 'form-control'}),
            'tirag': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'maket': forms.FileInput(attrs={'class': 'form-control'}),
            'dead_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'is_vip': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'delivery': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control'}),
            'order_temp': forms.Textarea(attrs={'class': 'form-control'}),


         }

