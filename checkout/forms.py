from django import forms
from .models import Information

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1,12)]
    YEAR_CHOICES = [(i, i) for i in range(2020,2040)]
    
    long_card_number = forms.CharField(label = 'Credit card number', required = False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    cvv = forms.CharField(label = 'Security code (CVV)', required = False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ('first_name', 'last_name', 'email', 'country', 'country', 'address', 'postcode',)