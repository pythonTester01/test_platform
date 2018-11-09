import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Model
from interface_app.models import TestCase
from interface_app.forms import TestCaseForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.

@login_required
def case_manage(request):

    if request.method == "GET":
        case_list = TestCase.objects.all().order_by("name")

        paginator = Paginator(case_list,5)

        page = request.GET.get("page")
        try:
            contacts = paginator.get_page(page)
        except EmptyPage:
            contacts = paginator.page(1)
        except PageNotAnInteger:
            contacts = paginator.page(paginator.num_pages)
        return render(request,"case_manage.html",{"type":"list","contacts": contacts})
    else:
        return "404"

@login_required
def api_debug(request):
    '''创建调试接口'''
    if request.method == "POST":
        api_url = request.POST.get("api_url")
        req_mode = request.POST.get("req_mode") #GET POST
        par_type = request.POST.get("par_type") #data json
        api_header = request.POST.get("api_header")
        api_parameter = request.POST.get("api_parameter")




        if api_header == "":
            api_header = "{}"
        if api_parameter == "":
            api_parameter= "{}"
        #if par_type != "json":
        #param = json.loads(api_parameter.replace("'", "\""))
        #api_header = json.loads(api_header.replace("'", "\""))

        #data = ""
        if req_mode == "get":
            data = requests.get(api_url, params=api_parameter)
        if req_mode == "post":
            data = requests.post(api_url, data=api_parameter)


        # if req_mode == "put":
        #     data = requests.put(api_url, params=param,header=api_header)
        # if req_mode == "delete":
        #     data = requests.delete(api_url, params=param,header=api_header)
        return HttpResponse(data.text.encode("utf-8"))





#创建接口
@login_required
def debug(request):
    if request.method == "GET":
        form = TestCaseForm()
        return render(request, "api_debug.html", {
            "type": "debug","form":form
        })
    else:
        return HttpResponse("404")

#保存测试用例
@login_required
def save_case(request):
    if request.method == "POST":
        mid = request.POST.get("mid","")
        api_name = request.POST.get("api_name","")
        api_url = request.POST.get("api_url","")
        req_mode = request.POST.get("req_mode","")
        par_type = request.POST.get("par_type","")
        api_header = request.POST.get("api_header","")
        api_parameter = request.POST.get("api_parameter","")

        if api_url == "" or req_mode =="" or par_type=="" or mid =="":

            return HttpResponse("必传参数为空！")

        if api_header == "":
            api_header = "{}"
        if api_parameter == "":
            api_parameter = "{}"

        module_obj = Model.objects.get(id=mid)

        case_data = TestCase.objects.create(module=module_obj,
                                name=api_name,url=api_url,
                                req_methed=req_mode,req_type=par_type,
                                req_header=api_header,req_para=api_parameter)


        if case_data is not None:
            return HttpResponse("1")

    else:
        return HttpResponse("404")

@login_required
def del_case(request):
    '''删除用例'''
    id = request.POST.get('id')
    TestCase.objects.filter(id=id).delete()
    return HttpResponse('1')

@login_required
def edit_case(request,mid):
    '''项目用例功能'''
    if request.method == "POST":
        form = TestCaseForm(request.POST)
        if form.is_valid():
            eid = form.cleaned_data["eid"]
            print(eid)
            module_obj = Model.objects.get(id=eid)
            module = form.cleaned_data[module_obj],
            name = form.cleaned_data["api_name"]
            url = form.cleaned_data["api_url"]
            req_methed = form.cleaned_data["req_mode"]
            req_type = form.cleaned_data["par_type"]
            req_header = form.cleaned_data["api_header"]
            req_para = form.cleaned_data["api_parameter"]
            TestCase.objects.filter(id=mid).update(module=module, name=name, url=url,req_methed=req_methed
                    ,req_type=req_type,req_header=req_header,req_para=req_para)
            return HttpResponseRedirect('/interface/case_manage/')
    else:
        if mid:
            form = TestCaseForm(instance = TestCase.objects.filter(id=mid).first())


    return render(request, "api_edit_debug.html", {"type": "edit", "form": form, "id": mid})
    #return render(request, "api_debug.html", {"type": "edit", "form": form, "id": mid})

