from distutils.command.upload import upload
from unicodedata import category
from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .forms import CustomUserManager
# Create your models here.
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

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    pub_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
            return self.category_name

# profile class
class Profile(models.Model): 
    user = models.OneToOneField(StudentUser, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    pub_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
       return self.user.username 


class Post(models.Model):
    title = models.CharField(max_length=260)
    article = HTMLField(blank=True)
    video = models.FileField(upload_to='media/',blank=True,null=True)
    audio_track = models.FileField(upload_to='post/', blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    pub_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
      
    def __str__(self):
       return self.title




class Review(models.Model):
    review = models.TextField()
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    pub_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.profile.user.username

# Review subclass
class ReviewThread(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    content = models.TextField()
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    pub_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    user =models.ForeignKey(StudentUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class WishList(models.Model):
   post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
   profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
