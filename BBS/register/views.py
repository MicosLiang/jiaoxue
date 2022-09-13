from django.shortcuts import render
from django.http import HttpResponse
from login import admin
import json


# Create your views here.
def register(request):
    un = request.GET.get('username')
    pw = request.GET.get('password')
    try:
        userNew = admin.models.user.objects.get(username=un)
        ans = {
            'status_code': -2,
            'ans': 'user existed',
        }
        return HttpResponse(json.dumps(ans))
    except Exception as e:
        userNew = admin.models.user(username=un, password=pw)
        userNew.save()
        ans = {
            'status_code': 200,
            'ans': 'success',
        }
        return HttpResponse(json.dumps(ans))