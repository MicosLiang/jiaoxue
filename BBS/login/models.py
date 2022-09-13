from django.db import models
from django.utils import timezone as django_tz

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    loginTime = models.DateTimeField(auto_now=True)#上次登录时间
    
class postData(models.Model):
    postId = models.CharField(max_length=20,default="null")
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=225,default="null")#帖子内容
    postTime = models.DateTimeField(auto_now=True)#上次登录时间
class reviewData(models.Model):
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=225,default="null")
    reviewTime = models.DateTimeField(auto_now=True)#上次登录时间
    reviewId = models.CharField(max_length=20,default="null")