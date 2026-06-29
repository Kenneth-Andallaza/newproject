from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    scheduled_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service address'}))
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional notes', 'rows': 4}))

    class Meta:
        model = Booking
        fields = ['scheduled_date', 'scheduled_time', 'address', 'notes']
