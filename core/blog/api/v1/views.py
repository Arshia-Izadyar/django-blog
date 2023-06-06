from rest_framework.views import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from blog.models import BlogPostModel
from .serializer import BlogPostSerializer
from .pagination import BlogPaginator


class BlogPostListApiView(ListCreateAPIView):
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = BlogPaginator
    # TODO: support multiple pages
    
class GetBlogPostApiView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPostModel.objects
    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticated, )
    

    