from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.db import models
from django.utils.crypto import get_random_string
from django.dispatch import receiver
import os


def create_id():
    return get_random_string(length=10)


def get_user_image_path(instance, filename):
    extends = filename.split('.')[-1]
    return os.path.join('user', f"{instance.id}.{extends}")


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser):
    id = models.CharField(default=create_id, primary_key=True, max_length=10)
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True, upload_to=get_user_image_path,
                            default='user/l_e_others_500.png')
    following = models.ManyToManyField("self", blank=True, related_name="followed_by", symmetrical=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True, max_length=150)
    birthday = models.DateField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user_id=kwargs['instance'])
