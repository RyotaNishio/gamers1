# Generated by Django 3.2.5 on 2022-03-23 09:39

import base.models.post_models
import base.models.user_models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=base.models.user_models.create_id, max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('data_joined', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(blank=True, default='user/l_e_others_500.png', null=True, upload_to=base.models.user_models.get_user_image_path)),
                ('following', models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base.user')),
                ('bio', models.TextField(blank=True, default='', max_length=150)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default=base.models.user_models.create_id, max_length=10, primary_key=True, serialize=False)),
                ('body', models.TextField(blank=True, default='', max_length=150)),
                ('img', models.ImageField(blank=True, null=True, upload_to=base.models.post_models.get_post_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
