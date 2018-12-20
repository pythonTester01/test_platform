from interface_app.extend.task_thread import TaskThread
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from interface_app.models import TestTask,TestResult
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

@login_required
def delete_task(request):
    if request.method == "POST":
        id = request.POST.get("id", "")
        if id == "":
            return common.response_failed("删除失败，ID不存在")
        TestTask.objects.filter(id=id).delete()
        return common.response_succeed(message="删除成功")
    else:
        return common.response_failed("请求方法错误!")

@login_required
def task_result(request):
    '''任务结果'''
    if request.method == "POST":
        id = request.POST.get("id", "")

        result_obj = TestResult.objects.get(id=id)

        data={
           "result":result_obj.result
        }
        return common.response_succeed(message="获取数据成功！",data=data)
    else:
        return common.response_failed(message="请求方法错误！")

@login_required
def run_task(request):
    '''运行任务i'''
    if request.method =="POST":
        id = request.POST.get("id","")

        if id =="":
            return common.response_failed("任务id不能为空")

        task_obj = TestTask.objects.all()
        runing_task = 0
        for i in task_obj:
            if i.status == 1:
                runing_task = 1
                break
        if runing_task == 1:
            return common.response_failed("当前有任务正在执行...")
        else:
            TaskThread(id).run_new()
            return common.response_succeed(message="已执行")
    else:
        return common.response_failed("请求方法错误")
