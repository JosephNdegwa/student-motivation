from distutils.command.upload import upload
from email.mime import audio
from sre_parse import CATEGORIES
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


class Post(models.Model):
    title = models.CharField(max_length=260)
    article = HTMLField()
    video = models.FileField(upload_to = 'post/',blank=True)
    audio_track = models.FileField(upload_to = 'post/',blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50,choices=category,default='Fullstack')