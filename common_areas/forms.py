from django import forms
from datetime import date, timedelta, datetime

_FORM_DATE_FORMAT = "%Y-%m-%d"

def get_min_date_today()->str:
    today = date.today().strftime(_FORM_DATE_FORMAT)
    return today
def get_max_date(days: int=365)->str:
    one_year = (
        datetime.utcnow() + 
        timedelta(days=days)
        ).strftime(_FORM_DATE_FORMAT)
    return one_year

class CommonAreaReservationForm(forms.Form):
    reservation_date = forms.DateField(
        required=True,
        label="Fecha de tu reservacion",
        widget=forms.DateInput(
                attrs={
                        "class": "form-control",
                        "min": get_min_date_today(),
                        "max": get_max_date(),
                        "type": "date",
                        "name": "reservation_date",
                        "id": "reservation_date",
                        "value": get_max_date(7)
                    }
            )
        )
    confirmation_email = forms.EmailField(
            required=False,
            label="E-Mail de confirmacion",
            widget=forms.EmailInput(
                attrs={
                    "id": "confirmation_email",
                    "name": "confirmation_email",
                    "class": "form-control",
                    "placeholder": "e-mail"
                }
            )
        )
    
    