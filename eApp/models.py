from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Cvideo(models.Model):
    cls = models.IntegerField()
    sub = models.CharField(max_length = 50)
    chpNo = models.IntegerField()
    title = models.CharField(max_length = 100)
    link = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
