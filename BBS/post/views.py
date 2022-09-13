from django.shortcuts import render
from django.http import HttpResponse
from login import admin
import json
import datetime
from django.utils.timezone import localtime
from . import createRandon
# Create your views here.
def createPost(request):
    try:
        data = json.loads(request.body)
        un = data.get('username')
        post = data.get('post')
        now = datetime.datetime.now()
        userNew = admin.models.user.objects.get(username=un)
        loginTime=localtime(userNew.loginTime)#转化为本地时间
        if(loginTime.year==now.year and loginTime.month==now.month and loginTime.day==now.day):#还在同一天
            rs = createRandon.RandomString(16)
            id = rs.create()#随机生成16位字符串
            exist=True
            while exist:#查询是否存在相同id
                try: 
                    admin.models.postData.objects.get( postId = id)
                    id = rs.create()
                except Exception as e:
                    exist=False
            new_post = admin.models.postData(content = post,postId=id,postTime=now,username=un)
            new_post.save()
            ans = {
                "status_code" : 200,
                "ans":post
            }
            return(HttpResponse(json.dumps(ans)))
        else:
            ans={
                "status_code" : -2,
                'Info':'login-time-out'
            }
            return(HttpResponse(json.dumps(ans)))
    except Exception as e:
        ans = {
            'status_code': -1,
            'ans': 'fail to find user',
        }
        print(str(e))
        return HttpResponse(json.dumps(ans))
def post(request):
    try:
        dat=admin.models.postData.objects.order_by('postTime')
        text=[]
        for each in dat:
            e={
                'username':each.username,
                'post':each.content
            }
            text.append(e)
        ans={
            'status_code':200,
            'ans':'ok',
            'text':text,
        }
        return HttpResponse(json.dumps(ans))
    except Exception as e:
        ans={
            'status_code':-1,
            'ans':'fail'
        }
        print(str(e))
        return HttpResponse(json.dumps(ans))
    

