import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from interface_app.models import TestTask
from project_app.models import Project,Model


from common.page_help import page
from test_platform import common
# Create your views here.

@login_required
def save_task_data(request):

    if request.method == "POST":
        name = request.POST.get("task_name","")
        describe = request.POST.get("task_describe","")
        cases = request.POST.get("task_cases","")
        if name == "":
            return common.response_failed("任务名称不能为空！")
        task = TestTask.objects.create(name=name,describe=describe,cases=cases)

        if task is not None:
            return common.response_succeed("保存成功！")
        return common.response_failed("保存出错！")
    else:
        return common.response_failed("请求方法错误！")

