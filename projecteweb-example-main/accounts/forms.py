# forms.py
from django import forms
from movied.models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['showtime', 'num_tickets']
        widgets = {
            'showtime': forms.Select(choices=[
                ('18', '18:00'),
                ('20', '20:00'),
                ('22', '22:00'),
            ], attrs={'id': 'showtime', 'required': True}),
            'num_tickets': forms.NumberInput(attrs={'id': 'num_tickets', 'min': 1, 'max': 10, 'required': True}),
        }
