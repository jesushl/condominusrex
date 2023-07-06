from models import Score
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class CreateScoreForm(forms.ModelForm):

    date_production = forms.DateField(widget=AdminDateWidget(attrs={'placeholder': 'Production'}), required=False)
    date_shipping = forms.DateField(widget=AdminDateWidget(attrs={'placeholder': 'Shipping'}), required=False)
    date_payment = forms.DateField(widget=AdminDateWidget(attrs={'placeholder': 'Payment'}), required=False)

    class Meta:
        model = Score
        fields = ['date_production', 'date_shipping', 'date_payment',]