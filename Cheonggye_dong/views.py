from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import appkey
import busstation as bs
from Cheonggye_dong.models import Bus
from django.core import serializers
import json

def index(request):
    key = appkey.getkey()
    context = { "appkey":key }
    return render(request, 'Cheonggye_dong/index.html', context)

def busstation(request):
    loc = request.GET.getlist("loc[]")
    result = bs.get_stations(loc)

    bus_result = result[1]
    station_result = result[0]
    
    print("view 출력------------------------------------------------")
    context = { 
        "bus_result":bus_result,
        "station_result":station_result
        }

    context2 =  json.dumps(context)
    return HttpResponse(context2, content_type="text/json-comment-filtered")
