import phonenumbers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
import templates
from Website import forms


class DenemeView(TemplateView):
    template_name = 'edit.html'

    def get(self, request):
        return render(request, self.template_name)


class LoginPageView(TemplateView):
    template_name = "Login.html"

    def get(self, request):
        login_form = forms.LoginForm()
        return render(request, self.template_name, context={"form": login_form})

    def post(self, request):
        print(request)
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email_and_phone = login_form.cleaned_data['email_and_phone']
            user = None
            if "@" in email_and_phone:
                user = User.objects.get(email=email_and_phone)
            else:
                try:
                    email_and_phone = phonenumbers.parse(email_and_phone, None)
                    user = User.objects.get(profile__phoneNumber=email_and_phone)
                except:
                    login_form = forms.LoginForm()
                    return render(request, self.template_name,
                                  context={"form": login_form, 'failed': True, 'phone': True})
            password = login_form.cleaned_data['password']
            authenticated_user = authenticate(username=user.username, password=password)
            if authenticated_user is not None:
                return HttpResponse('Successful Login')
            else:
                return render(request, self.template_name,
                              context={"form": login_form, 'failed': True, 'password': True})
        return HttpResponseRedirect('/login/')
