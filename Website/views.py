import phonenumbers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView
from Website import forms


class UsersView(TemplateView):
    template_name = 'Users.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, template_name=self.template_name, context={'users': users})


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
                try:
                    user = User.objects.get(email=email_and_phone)
                except:
                    return render(request, self.template_name, context={'form': login_form, 'failed': True})
            else:
                try:
                    email_and_phone = phonenumbers.parse(email_and_phone, None)
                    user = User.objects.get(profile__phoneNumber=email_and_phone)
                except:
                    return render(request, self.template_name,
                                  context={"form": login_form, 'failed': True, 'number': True})
            password = login_form.cleaned_data['password']
            authenticated_user = authenticate(username=user.username, password=password)
            if authenticated_user is not None:
                return HttpResponseRedirect('/successfulLogin/')
            else:
                return render(request, self.template_name,
                              context={"form": login_form, 'failed': True, 'password': True})
        return HttpResponseRedirect(reverse('Login'))


class SuccessfulLoginView(TemplateView):
    template_name = 'SuccessfulLogin.html'

    def get(self, request):
        return render(request, template_name=self.template_name)
