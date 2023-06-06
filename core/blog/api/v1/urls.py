from django.urls import path
from .views import BlogPostListApiView, GetBlogPostApiView

app_name = 'api'

urlpatterns = [
    path('list/', BlogPostListApiView.as_view(), name="post-list"),
    path('post/<int:pk>/', GetBlogPostApiView.as_view(), name="post-detail"),
]
