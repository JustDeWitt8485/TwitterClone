# Generated by Django 3.1.4 on 2020-12-07 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweets',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='tweets',
            name='upvote',
        ),
    ]
