from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    lastTime = models.DateTimeField(auto_now_add=True)#上次登录时间
    
class postData(models.Model):
    content = models.CharField(max_length=225,default="null")#帖子内容