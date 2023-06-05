from typing import Any
from django import http
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView, DetailView, View
from django.urls import reverse_lazy
from .models import BlogPostModel, CommentModel
from .forms import CreateBlogPostForm, CommentForm
from django.shortcuts import get_object_or_404


# CrEaTe YoUr ViEeS HeRe .


class BlogPostList(ListView):
    queryset = BlogPostModel.objects.filter(state=2)
    template_name = 'blog/blog_post_list.html'
    context_object_name  = 'posts'
    
    
class BlogPostCreate(FormView):
    
    form_class = CreateBlogPostForm
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
