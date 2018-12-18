import json
import os
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from interface_app.models import TestTask,TestCase,TestResult

from interface_app.extend.task_thread import TaskThread

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
       TaskThread(tid).run_new()
       return HttpResponseRedirect("/interface/task_manage/")
    else:
        return HttpResponse("404")

#查看任务列表
@login_required
def task_result_list(request,tid):
    if request.method == "GET":

        task_obj = TestTask.objects.get(pk=tid)
        result_list = TestResult.objects.filter(task_id=tid)

        return render(request,"task_result.html",
                      {"type":"result",
                       "result_list":result_list,
                        "task_obj":task_obj})
    else:
        return HttpResponse("404")

