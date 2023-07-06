from django import forms

from .models import Client, Addressee, Payment


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client 
        fields = '__all__'
        widgets = {
            'local_phone': forms.NumberInput(
                attrs={'maxlength': "11",},
            ),
        }

class AddresseeForm(forms.ModelForm):
    class Meta:
        model = Addressee
        fields = ['data_addressee', 'destiny', 'photo', 'google_map',]

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount',]

