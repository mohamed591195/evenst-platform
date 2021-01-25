from django import forms
from .models import Event

class AddEventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }