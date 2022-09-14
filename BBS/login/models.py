from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    lastLogin = models.CharField(max_length=114514, default=-1)
    loginid = models.CharField(max_length=20, default=-1)

class postData(models.Model):
    postId = models.CharField(max_length=20, default="null")
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=225, default="null")  # 帖子内容
    postTime = models.DateTimeField(auto_now=True)  # 上次登录时间


class reviewData(models.Model):
    username = models.CharField(max_length=20)
    content = models.CharField(max_length=225, default="null")
    reviewTime = models.DateTimeField(auto_now=True)  # 上次登录时间
    reviewId = models.CharField(max_length=20, default="null")
