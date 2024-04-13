from django import forms

class RegisterForm(forms.Form):
    firstname = forms.CharField(min_length=1,label="First name")
    lastname = forms.CharField(min_length=1,label="Last name")