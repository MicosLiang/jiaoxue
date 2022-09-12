from django.shortcuts import render
from django.http import HttpResponse
from login import admin
import json
import datetime
from django.utils.timezone import localtime
# Create your views here.
def post(request):
    try:
        data = json.loads(request.body)
        un = data.get('username')
        post = data.get('post')
        now = datetime.datetime.now()
        userNew = admin.models.user.objects.get(username=un)
        lastTime=localtime(userNew.lastTime)#转化为本地时间
        if(lastTime.year==now.year and lastTime.month==now.month and lastTime.day==now.day):#还在同一天
            new_post = admin.models.postData(content = post)
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
    
    

