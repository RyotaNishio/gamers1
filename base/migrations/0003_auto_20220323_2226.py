# Generated by Django 3.2.5 on 2022-03-23 13:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220323_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
    ]