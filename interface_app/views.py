import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def case_manage(request):

    if request.method == "GET":
        return render(request,"case_manage.html",{"type":"list"})
    else:
        return "404"

@login_required
def api_debug(request):
    '''创建调试接口'''
    if request.method == "POST":
        api_name = request.POST.get("api_name")
        api_url = request.POST.get("api_url")
        req_mode = request.POST.get("req_mode")
        par_type = request.POST.get("par_type")
        api_header = request.POST.get("api_header")
        api_parameter = request.POST.get("api_parameter")



        if api_header is None:
            pass
        if api_parameter is None:
            api_parameter={}
        param = json.loads(api_parameter.replace("'", "\""))



        if req_mode =="get":
            r = requests.get(api_url)
        if req_mode == "post":
            r = requests.post(api_url, params=param,header=api_header)
        # if req_mode == "put":
        #     data = requests.put(api_url, params=param,header=api_header)
        # if req_mode == "delete":
        #     data = requests.delete(api_url, params=param,header=api_header)


        return HttpResponse(r.text.encode("utf-8"))




#创建接口
@login_required
def debug(request):
    if request.method == "GET":
        return render(request, "api_debug.html", {
            "type": "debug"
        })
    else:
        return HttpResponse("404")
