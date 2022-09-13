from django.shortcuts import render
from django.http import HttpResponse
from login import admin
import json
import datetime
from django.utils.timezone import localtime
# Create your views here.
def review(request):
    try:
        data = json.loads(request.body)
        un = data.get('username')
        review = data.get('review')
        now = datetime.datetime.now()#获取当前时间
        userNew = admin.models.user.objects.get(username=un)
        lastTime=localtime(userNew.lastTime)#转化为本地时间
        if(lastTime.year==now.year and lastTime.month==now.month and lastTime.day==now.day):#还在同一天
            new_review = admin.models.reviewData(content = review)
            new_review.save()
            ans = {
                "status_code" : 200,
                "ans":review
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