from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
# CrEaTe YoUr MoDeLd HeRe ................


class IsActiveManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()


class CommentModel(models.Model):
    blog = models.ForeignKey('BlogPostModel', on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comments")
    spoiler = models.BooleanField(default=False)



class BlogPostModel(models.Model):
    DRAFT = 1
    POSTED = 2
    states = (
        (DRAFT, "draft"),
        (POSTED, "posted"),
    )
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts')
    content = models.TextField()
    # TODO: add support for content 
    state = models.PositiveSmallIntegerField(choices=states, default=DRAFT)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    comments = models.ManyToManyField(CommentModel, related_name="blog_comments", blank=True)
    title = models.CharField(max_length=35, unique=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)


    
    
    objects = IsActiveManager()
    default_manager = models.Manager()

        
    def __str__(self):
        return str(self.title)
    
