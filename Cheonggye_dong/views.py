from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import appkey
import busstation as bs

def index(request):
    key = appkey.getkey()
    context = { "appkey":key }
    return render(request, 'Cheonggye_dong/index.html', context)

def busstation(request):
    la1 = request.GET.get("la1")
    la2 = request.GET.get("la2")
    lo1 = request.GET.get("lo1")
    lo2 = request.GET.get("lo2")
    result = bs.get_stations(la1,la2,lo1,lo2)
    print("view 출력------------------------------------------------")
    print(la1)
    print(type(la1))
    # context = { "busstations":result }
    return HttpResponse(result)
    # return render(request, 'Cheonggye_dong/index.html', context)
