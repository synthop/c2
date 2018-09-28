from django import forms

class SendForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    ertetert