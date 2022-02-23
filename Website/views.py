import phonenumbers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import templates
from Website import forms


class LoginPageView(TemplateView):
    template_name = "Login.html"

    def get(self, request):
        login_form = forms.LoginForm()
        return render(request, self.template_name, context={"form": login_form, })

    def post(self, request):
        print(request)
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email_and_phone = login_form.cleaned_data['email_and_phone']
            user = None
            if "@" in email_and_phone:
                user = User.objects.get(email=email_and_phone)
            else:
                email_and_phone = phonenumbers.parse(email_and_phone, None)
                user = User.objects.get(profile__phoneNumber=email_and_phone)
            password = login_form.cleaned_data['password']
            authenticated_user = authenticate(username=user.username, password=password)
            if authenticated_user is not None:
                return HttpResponse("Able to Login - No other Page Here")
            else:
                return HttpResponse("Not Able to Login - No other Page Here")
        return HttpResponse("Hello World")
