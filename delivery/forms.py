from django import forms
from django.forms import widgets

from .models import Delivery
from .choices import service_type2


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'addressee_data',  'destiny', 'date',
            'type_delivery', 'preferred_price', 'type_service',
            'status_delivery', 'recieved_money',
            'status_recieved_money', 'distributing',
        ]
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#reservationdatetime',
                    'type': 'date',
                },
            )
        }



class DeliveryAddresseeForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'type_delivery',   'type_service', 'date',
            'status_delivery', 'recieved_money',
            'status_recieved_money', 'distributing',
        ]
        widgets = {
            'date': forms.SelectDateWidget()
        }


class DeliveryEditForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'addressee_data',  'destiny', 'date',
            'type_delivery', 'preferred_price', 'type_service',
            'status_delivery', 'recieved_money',
            'status_recieved_money', 'distributing',
        ]
