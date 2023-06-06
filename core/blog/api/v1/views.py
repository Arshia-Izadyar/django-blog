from rest_framework.views import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from blog.models import BlogPostModel
from .serializer import BlogPostSerializer
from .pagination import BlogPaginator


class BlogPostListApiView(ListCreateAPIView):
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = BlogPaginator
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('state', )
    search_fields = ('author__username', 'title')
    ordering_fields = ('created_date', 'modify_date')
    
    # filter_queryset = BlogPostModel.objects.aggregate(
class GetBlogPostApiView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPostModel.objects
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticated, )

    

    