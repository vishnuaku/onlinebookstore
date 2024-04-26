from django import forms
class PaymentForm(forms.Form):
    transid = forms.NumberInput()