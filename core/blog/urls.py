from django.urls import path
from django.views.generic import TemplateView
from .views import BlogPostList, BlogPostCreate, BlogPostDetail, CommentCreateView, EditPostView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="blog/about.html"), name='about-page'),
    
    path('posts/', BlogPostList.as_view(), name='posts-list'),
    path('detail/<int:pk>/comment-create/', CommentCreateView.as_view(), name='comment_create'),
    
    path('edit/<int:pk>/', EditPostView.as_view(), name='edit-post'),
    path('create/', BlogPostCreate.as_view(), name='create-post'),
    path('detail/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    # create read update delete 
]
