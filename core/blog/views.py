from typing import Any
from django import http
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, DetailView, View, UpdateView
from django.urls import reverse_lazy
from .models import BlogPostModel, CommentModel
from .forms import BlogPostForm, CommentForm
from django.core.exceptions import ValidationError
from datetime import datetime


# CrEaTe YoUr ViEeS HeRe .


class BlogPostList(ListView):
    queryset = BlogPostModel.objects.filter(state=2)
    template_name = 'blog/blog_post_list.html'
    context_object_name  = 'posts'
    
    
class BlogPostCreate(FormView):
    
    form_class = BlogPostForm
    success_url = reverse_lazy('posts-list')
    template_name = 'blog/blog_post_create.html'

    @method_decorator(login_required(login_url="login"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)
    

class BlogPostDetail(DetailView):
    model = BlogPostModel
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'post'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = CommentModel.objects.filter(blog=self.object)
        return context

class CommentCreateView(View):
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.blog = BlogPostModel.objects.get(pk=self.kwargs['pk'])
            comment.save()
        return redirect('posts-list')

class EditPostView(UpdateView):
    model = BlogPostModel
    fields = ('title', 'content', 'state', 'image')
    success_url = reverse_lazy("posts-list")
    template_name = 'blog/update_post.html'
    context_object_name = 'post'
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, *args, **kwargs):
        if request.user == self.object.author:
            return super().get(request, *args, **kwargs)
        else:raise ValidationError("user is not owner of blog post")
        
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.form = BlogPostForm(request.POST, self.model)
        self.modify_date = datetime.now()
        # self.form.is_valid()
        # self.form.save()
        
        return super().post(request, *args, **kwargs)