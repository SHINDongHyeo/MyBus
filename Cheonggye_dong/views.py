from django.shortcuts import render
from django.http import HttpResponse
import appkey
import busstation as bs

def index(request):
    key = appkey.getkey()
    context = { "appkey":key }
    return render(request, 'Cheonggye_dong/index.html', context)

def busstation(request):
    result = bs.get_stations()
    print("------------------------------------------------")
    print(result)
    context = { "busstations":result }
    return HttpResponse(result)
    # return render(request, 'Cheonggye_dong/index.html', context)