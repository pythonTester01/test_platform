from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

from common.page_help import page
from project_app.forms import ProjectForm
from project_app.models import Project

# Create your views here.

'''
默认值转换为int
'''
def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception as e:
        arg = default
    return arg

@login_required #判断用户是否登录
def project_manage(request):
    '''项目列表'''

    project_data = Project.objects.all().order_by("-create_time")

    contacts = page(request,project_data)

    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "project_manage.html", {"user": username,"contacts":contacts,
                                                   "type":"list"})
def search_project(request):
    if request.method == "GET":
        search_project = request.GET.get("search_project","")
        project_data = Project.objects.filter(title__icontains=search_project)
        contacts = page(request, project_data)
        return render(request, "project_manage.html",
                      {"type": "list", "contacts": contacts, "search_project": search_project})
    else:
        return "404"
# @login_required
# def project_model(request):
#     '''
#     判断id是否为空，如果空，跳转添加页面，否则回显数据，变为修改页面。
#     '''
#     id = request.GET.get('id')
#     print(id)
#     if id is not None:
#         project_data = Project.objects.filter(id=id).first()
#         return render(request, "project_manage.html",{"project_data":project_data,"type":"edit"})
#     else:
#         return render(request, "project_manage.html",{"type":"add"})
#
# #项目管理-添加
# @login_required
# def project_model_add(request):
#     title = request.POST.get('title')
#     describe = request.POST.get('describe')
#     create_time = request.POST.get('create_time')
#     status = request.POST.get('status')
#     if status == "1":
#         status = True
#     else:
#         status = False
#     print(title,describe,create_time,status)
#     Project.objects.create(title=title, describe=describe, create_time=create_time,status=status)
#     return HttpResponseRedirect('/manage/project_manage/')
#
# #项目管理-删除（根据id删除）
# @login_required
# def project_model_del(request):
#     id = request.POST.get('id')
#     Project.objects.filter(id=id).delete()
#     #return HttpResponseRedirect('/project_manage/')
#     return HttpResponse('1')
#
# #项目管理-更新
# @login_required
# def project_model_update(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         title = request.POST.get('title')
#         describe = request.POST.get('describe')
#         create_time = request.POST.get('create_time')
#         status = request.POST.get('status')
#         print(status)
#         if status == "1":
#             status = True
#         else:
#             status = False
#         Project.objects.filter(id=id).update(title=title, describe=describe, create_time=create_time,status=status)
#         return HttpResponseRedirect('/manage/project_manage/')


@login_required
def add_project(request):
    '''
    项目添加
    '''
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            describe =form.cleaned_data["describe"]
            status =form.cleaned_data["status"]
            Project.objects.create(title=title, describe=describe, status=status)
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        form = ProjectForm()
    return render(request, "project_manage.html", {"type": "add","form":form})


@login_required
def edit_project(request,pid):
    '''
    项目编辑功能
    '''
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            Project.objects.filter(id=pid).update(title=title, describe=describe,status=status)
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        if pid:
            form = ProjectForm(instance = Project.objects.filter(id=pid).first())
        #project_data = Project.objects.filter(id=pid).first()

    return render(request, "project_manage.html", { "type": "edit","form":form,"id":pid})

@login_required
def del_project(request):
    '''项目删除'''
    id = request.POST.get('id')
    Project.objects.filter(id=id).delete()
    return HttpResponse('1')







