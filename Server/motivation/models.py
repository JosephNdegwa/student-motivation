from distutils.command.upload import upload
from unicodedata import category
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
category=[('Fullstack','Fullstack'),
('DevOps','DevOps'),
('Front-End','Front-End')
]

class Staff(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id
        
    def __str__(self):

        return self.user.first_name



class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=260)
    article = HTMLField(blank=True)
    video = models.FileField(upload_to = 'post/',blank=True)
    audio_track = models.FileField(upload_to = 'post/',blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50,choices=category,default='Fullstack')

    