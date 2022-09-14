from django.shortcuts import render
from django.http import HttpResponse
from login import admin
import json
import time
import hashlib
import random


# Create your views here.
def register(request):
    randomNum = str(random.randint(0, 114514))
    loginID = hashlib.md5(randomNum.encode()).hexdigest()[8:-8]  # 生成随机登录id
    timeNow = time.time()  # 获取当前时间
    data = json.loads(request.body)
    un = data.get('username')  # 获取用户名
    pw = data.get('password')  # 获取密码
    try:
        userNew = admin.models.user.objects.get(username=un)  # 判断用户是否已经存在
        ans = {
            'status_code': -2,
            'ans': 'user existed',
        }
        return HttpResponse(json.dumps(ans))
    except Exception as e:
        userNew = admin.models.user(username=un, password=pw, lastLogin=timeNow, loginid=loginID)  # 在数据库中生成新用户
        userNew.save()
        ans = {
            'status_code': 200,
            'ans': 'success',
        }
        return HttpResponse(json.dumps(ans))
