from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, FormView, DetailView, View
from blog.models import BlogPostModel


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/blog/posts/'
    context_object_name = 'form'
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('next') is not None:
            self.success_url = request.GET.get('next')
        if request.user.is_authenticated is True :
            return redirect('posts-list')
        return super().dispatch(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request=self.request, username=username, password=password)
        if user is not None:
            login(request=self.request, user=user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
        
        
    def post(self, request, *args, **kwargs):
        
        return super().post(request, *args, **kwargs)
        

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('accounts:login')
    
    
class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.is_valid()
        form.save()
        return redirect('accounts:login')
    

class ProfileView(ListView):
    template_name = 'accounts/profile.html'
    # queryset = BlogPostModel.objects.all()
    # model = BlogPostModel
    
    
    @method_decorator(login_required) 
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        return super().dispatch(request, *args, **kwargs)
    
    
    def get_queryset(self):
        self.query = BlogPostModel.objects.filter(author=self.user)
        return self.query
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.query
        context['user'] = self.user
        context['totalposts'] = self.query.count()
        return context

    
        

    
    
    