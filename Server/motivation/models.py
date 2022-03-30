from distutils.command.upload import upload
from unicodedata import category
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .forms import StaffUserManager
# Create your models here.
category = [('Fullstack', 'Fullstack'),
            ('DevOps', 'DevOps'),
            ('Front-End', 'Front-End')
            ]
class StudentUser(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    STUDENT = 2

    USER_ROLE_CHOICES = (
        (ADMIN, 'Staff'),
        (STUDENT, 'Student'),
    )
    username = models.CharField(unique=True,max_length=20)
    first_name = models.CharField(max_length=30, blank=True,null=True)
    last_name = models.CharField(max_length=50, blank=True,null=True)
    email = models.EmailField()
    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, blank=True, null=True, default=2)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    modified_by = models.EmailField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = StaffUserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=260)
#     article = HTMLField(blank=True)
#     video = models.FileField(upload_to='post/', blank=True)
#     audio_track = models.FileField(upload_to='post/', blank=True)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     category = models.CharField(
#         max_length=50, choices=category, default='Fullstack')
