from django.db import models
from django.forms import CharField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    
 
    def __str__(self):
        return self.name