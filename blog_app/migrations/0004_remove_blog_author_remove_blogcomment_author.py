# Generated by Django 5.1 on 2024-09-03 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_alter_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='author',
        ),
    ]
