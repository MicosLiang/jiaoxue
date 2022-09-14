from django.shortcuts import render
from django.http import HttpResponse
from login import admin
import json
import datetime
import time
import random
import hashlib


# Create your views here.

def login(request):
    timeNow = time.time()  # 获取当前时间（以时间戳形式）
    randomNum = str(random.randint(0, 114514))
    loginID = hashlib.md5(randomNum.encode()).hexdigest()[8:-8]  # 生成随机登录id
    try:
        data = json.loads(request.body)
        un = data.get('username')  # 获取用户输入的用户名
        pw = data.get('password')  # 获取用户输入的密码
        user = admin.models.user.objects.get(username=un)  # 从数据库中得到对应用户的密码
        if pw == user.password:  # 两个密码相同，登录成功
            admin.models.user.objects.filter(username=un).update(lastLogin=timeNow, loginid=loginID)
            ans = {
                'status_code': 200,
                'ans': 'success',
                'lastlogin': timeNow,
                'loginid': loginID,
            }
        else:  # 反之不成功
            ans = {
                'status_code': -1,
                'ans': 'wrong password',
            }
    except Exception as e:  # 用户不存在
        ans = {
            'status_code': -1,
            'ans': 'user not existed',
        }
    return HttpResponse(json.dumps(ans))


def relogin(request):
    try:  # 用户存在，执行此代码
        data = json.loads(request.body)
        un = data.get('username')  # 获取用户名
        loginTime = data.get('lastlogin')  # 获取上次登录时间
        loginid = data.get('loginid')  # 获取登录id
        user = admin.models.user.objects.get(username=un)  # 判断用户是否存在
        if float(loginTime) - float(user.lastLogin) < 86400 and loginid == user.loginid:  # 两次登录时间小于24小时，且登录id相同，自动登录
            ans = {
                'status_code': 200,
                'ans': 'success',
            }
            return HttpResponse(json.dumps(ans))
        else:  # 反之，登录失败
            ans = {
                'status_code': -1,
                'ans': 'login fail',
            }
            return HttpResponse(json.dumps(ans))
    except Exception as e:  # 用户名不存在
        ans = {
            'status_code': -1,
            'ans': 'user not existed',
        }
        return HttpResponse(json.dumps(ans))
