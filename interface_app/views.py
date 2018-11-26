import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Model
from interface_app.models import TestCase
from project_app.models import Project,Model
from interface_app.forms import TestCaseForm
#from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from common.page_help import page
from test_platform import common
# Create your views here.

@login_required
def case_manage(request):

    if request.method == "GET":
        case_list = TestCase.objects.all().order_by("-create_time")

        contacts = page(request,case_list)
        # paginator = Paginator(case_list,5)
        #
        # page = request.GET.get("page")
        # try:
        #     contacts = paginator.get_page(page)
        # except EmptyPage:
        #     contacts = paginator.page(1)
        # except PageNotAnInteger:
        #     contacts = paginator.page(paginator.num_pages)
        return render(request,"case_manage.html",{"type":"list","contacts": contacts})
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
def add_case(request):
    if request.method == "GET":
        form = TestCaseForm()
        return render(request, "add_case.html", {
            "type": "add_case","form":form
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
    '''编辑/调试用例功能'''
    if request.method == "GET":
        print(mid)
        form = TestCaseForm()
        return render(request, "api_edit_debug.html",
                      {"type": "edit", "form": form, "mid": mid})
    else:
        return HttpResponse("404")


def get_case_info(request):
    '''用例调试页面数据回显接口'''
    if request.method=="POST":
        case_Id = request.POST.get('caseId',"")
        print(case_Id)
        if case_Id =="":
            return JsonResponse({'success':'flase','message':'ID is null!'})

        case_obj = TestCase.objects.get(pk=case_Id)

        module_obj = Model.objects.get(id=case_obj.module_id)

        module_name = module_obj.name  # 模块名称

        project_name = Project.objects.get(id=module_obj.project_id).title  # 项目名称

        case_info = {"moduleName": module_name,
                     "projectName": project_name,
                     "name": case_obj.name,
                     "url": case_obj.url,
                     "reqMethod": case_obj.req_methed,
                     "reqType": case_obj.req_type,
                     "reqHeader": case_obj.req_header,
                     "reqParameter": case_obj.req_para,
                     "assertText": case_obj.response_assert,
                     }

        return JsonResponse({'success':'true','message':'ok','data':case_info})
    else:
        HttpResponse('404')

def get_project_list(request):
    """
    获取项目模块列表
    :param request:
    :return: 项目接口列表
    """
    if request.method == "GET":
        project_list = Project.objects.all()
        data_list = []
        for project in project_list:
            project_dict = {
                "name": project.title
            }
            module_list = Model.objects.filter(project_id=project.id)
            if len(module_list) != 0:
                module_name = []
                for module in module_list:
                    module_name.append(module.name)

                project_dict["moduleList"] = module_name
                data_list.append(project_dict)

        return common.response_succeed(data=data_list)

    else:
        return common.response_failed("请求方法错误")

def update_case(request):
    """更新接口测试用例"""
    if request.method == "POST":
        case_id = request.POST.get("cid", "")
        name = request.POST.get("name", "")
        url = request.POST.get("req_url", "")
        method = request.POST.get("req_method", "")
        parameter = request.POST.get("req_parameter", "")
        req_type = request.POST.get("req_type", "")
        header = request.POST.get("header", "")
        module_name = request.POST.get("module", "")
        assert_text = request.POST.get("assert_text", "")


        if url == "" or method == "" or req_type == "" or module_name == "" or assert_text == "":
            return common.response_failed("必传参数为空")

        if parameter == "":
            parameter = "{}"

        if header == "":
            header = "{}"

        module_obj = Model.objects.get(name=module_name)
        case_obj = TestCase.objects.filter(id=case_id).update(
                module=module_obj,
                name=name,
                url=url,
                req_methed=method,
                req_header=header,
                req_type=req_type,
                req_para=parameter,
                response_assert=assert_text
            )
        if case_obj == 1:
            return common.response_succeed("更新成功！")
        else:
            return common.response_failed("更新失败！")
    else:
        return common.response_failed("请求方法错误")

def api_assert(request):
    """对测试用例的断言进行验证"""
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")

        if result_text == "" or assert_text == "":
            return common.response_failed("验证的数据不能为空")

        try:
            assert assert_text in result_text
        except AssertionError:
            return common.response_failed("验证失败!")
        else:
            return common.response_succeed("验证成功!")
    else:
        return common.response_failed("请求方法错误")
