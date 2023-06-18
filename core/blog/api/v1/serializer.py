from rest_framework import serializers
from blog.models import BlogPostModel, CommentModel
from rest_framework.reverse import reverse



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ('id', 'user', 'content', 'created_time')


class BlogPostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(method_name="get_abs_url")
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = BlogPostModel
        fields = '__all__'
        read_only_fields = ('id', 'author', 'modify_date', 'created_date')
        
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if request.parser_context.get('kwargs').get('pk', None) is None:
            rep.pop("comments")
            rep.pop("content")
            rep.pop('url')
        else:
            rep.pop("id")
        return rep
    
    
    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri()
    
    
    
