# Generated by Django 3.1.4 on 2020-12-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0007_remove_twitteruser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
