# Generated by Django 5.1.4 on 2024-12-20 14:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_author_postview_likeview_commentview_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentView',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='LikeView',
            new_name='Like',
        ),
        migrations.RenameModel(
            old_name='PostView',
            new_name='Post',
        ),
    ]
