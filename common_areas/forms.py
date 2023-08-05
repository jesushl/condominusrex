from django import forms

class CommonAreaReservationForm(forms.Form):
    reservation_date = forms.DateField(required=True)
    confirmation_email = forms.EmailField(required=False)