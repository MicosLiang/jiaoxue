from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import my_num

# Create your views here.

def sayhello(request):
    try:
        n1 = float(request.GET.get('n1'))
        n2 = float(request.GET.get('n2'))
        if n1 and n2:
            ans = {
                'status_code' : 200,
                'ans' : n1 / n2
            }
        else:
            ans = {
                'status_code' : -1,
                'ans' : 'n1 or n2 is null'
            }
    except Exception as e:
        ans = {
            'status_code' : -1,
            'ans' : str(e)
        }
    return(HttpResponse(json.dumps(ans)))


def addnum(request):
    try:
        num = request.GET.get('number')
        new_num = my_num()
        new_num.dat = num
        new_num.save()
        ans = {
            "status_code" : 200
        }
    except Exception as e:
        ans = {
            "status_code" : -1
        }
        print(str(e))
    all = my_num.objects.all()
    for each in all:
        print(each.dat)
    return(HttpResponse(json.dumps(ans)))