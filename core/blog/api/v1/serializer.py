from rest_framework import serializers
from blog.models import BlogPostModel


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = ('id', 'title', 'author', 'modify_date', 'created_date', 'state', 'content', 'comments')
        read_only_fields = ('id', 'author', 'comments', 'modify_date', 'created_date')
        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk', None) is None:
            rep.pop("comments")
            rep.pop("content")
        else:
            rep.pop("id")
        return rep