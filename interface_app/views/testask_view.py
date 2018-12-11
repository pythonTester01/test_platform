import json
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from interface_app.models import TestTask,TestCase

from interface_app.apps import TASK_PATH,RUN_TASK_FILE

from common.page_help import page

# Create your views here.

@login_required
def task_manage(request):

    if request.method == "GET":
        case_list = TestTask.objects.all().order_by("-create_time")

        contacts = page(request,case_list)

        return render(request,"task_manage.html",{"type":"list","contacts": contacts})
    else:
        return "404"

@login_required
def search_case(request):
    '''用例搜索功能'''
    if request.method == "GET":
        search_case = request.GET.get("search_case","")
        case_data = TestCase.objects.filter(name__icontains = search_case)
        contacts = page(request,case_data)
        return  render(request,"case_manage.html",{"type":"list","contacts": contacts,"search_case":search_case})
    else:
        return "404"


#创建接口
@login_required
def add_task(request):
    if request.method == "GET":
        return render(request, "add_task.html", {
            "type": "add"
        })
    else:
        return HttpResponse("404")

# 运行任务
@login_required
def run_task(request,tid):

    if request.method == "GET":
       task_obj = TestTask.objects.get(id=tid)

       case_list = task_obj.cases.split(",")
       case_list.pop(-1)
       #运行函数
       #run_cases()
       cases_all ={}
       for case_id in case_list:
           print(case_id)
           cases_obj = TestCase.objects.get(pk=case_id)

           case_dict={
               "url":cases_obj.url,
               "req_methed":cases_obj.req_methed,
               "req_type":cases_obj.req_type,
               "req_header":cases_obj.req_header,
               "req_para":cases_obj.req_para,
               "response_assert":cases_obj.response_assert
           }
           cases_all[cases_obj.id]=case_dict
       json_str = json.dumps(cases_all)
       case_data_file = TASK_PATH + "cases_data.json"
       with open(case_data_file,"w+") as f:
           f.write(json_str)

       #运行测试json文件
       os.system("python3 "+RUN_TASK_FILE)

       return HttpResponseRedirect("/interface/task_manage/")
    else:
        return HttpResponse("404")

