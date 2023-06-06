from django.contrib import admin

from .models import BlogPostModel
# CrEaTe YoUr MoDeLd HeRe ................

@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'state', 'author')
    list_filter = ('state',)
    search_fields = ('title',)
