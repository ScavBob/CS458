from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    email_and_phone = forms.CharField()

    class Meta:
        model = User
        fields = ('email_and_phone', 'password',)
