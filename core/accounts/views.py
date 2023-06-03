from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/blog/posts/'
    context_object_name = 'form'
    template_name = 'accounts/login.html'


    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request=self.request, username=username, password=password)
        if user is not None:
            login(request=self.request, user=user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        

class LogoutView(View):
    # template_name = 'accounts/logout.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')
    
    
class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.is_valid()
        form.save()
        return redirect('posts-list')