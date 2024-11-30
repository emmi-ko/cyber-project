from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password") 
        password2 = cleaned_data.get("password2")
        #validate_password(password)
        if password != password2:
            raise forms.ValidationError("Your passwords do not match")
        return cleaned_data





   
