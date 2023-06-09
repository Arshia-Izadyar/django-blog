# Generated by Django 3.2 on 2023-06-03 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpostmodel_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/blog')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_images', to='blog.blogpostmodel')),
            ],
        ),
    ]
