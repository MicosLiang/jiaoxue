from django.shortcuts import render
from django.http import HttpResponse
from . import admin
import json
import datetime

# Create your views here.

def login(request):
    try:
        un = request.GET.get('username')  # 获取用户输入的用户名
        pw = request.GET.get('password')  # 获取用户输入的密码
        user = admin.models.user.objects.get(username=un)  # 从数据库中得到对应用户的密码
        now = datetime.datetime.now()
        if pw == user.password:  # 两个密码相同，登录成功
            ans = {
                'status_code': 200,
                'ans': 'success',
            }
            user.save()
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
