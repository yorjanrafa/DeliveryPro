from django import forms

from .models import Worker

class WorkerForm(forms.ModelForm):
    class Meta:
        model =Worker 
        fields = ['name', 'last_name']

