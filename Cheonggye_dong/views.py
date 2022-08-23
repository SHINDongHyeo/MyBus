from django.shortcuts import render
from django.http import HttpResponse
import appkey

def index(request):
    appkey = appkey.getkey()
    context = { "appkey":appkey }
    return render(request, 'Cheonggye_dong/index.html', context)