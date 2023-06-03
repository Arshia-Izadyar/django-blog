from django import forms
from .models import CommentModel, BlogPostModel


class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ('title', 'content', 'state', 'image')
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('content', 'spoiler')