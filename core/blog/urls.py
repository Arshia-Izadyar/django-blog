from django.urls import path
from .views import BlogPostList, BlogPostCreate, BlogPostDetail, CommentCreateView

urlpatterns = [
    path('posts/', BlogPostList.as_view(), name='posts-list'),
    # create
    path('create/', BlogPostCreate.as_view(), name='create-post'),
    # detail and comment
    path('detail/<int:pk>/', BlogPostDetail.as_view(), name='post-detail'),
    # path('detail/<int:pk>/create/', CommentCreateView.as_view(), name='comment_create'),
    path('detail/<int:pk>/comment-create/', CommentCreateView.as_view(), name='comment_create'),

    
]
