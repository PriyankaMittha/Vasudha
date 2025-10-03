from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300, null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    

