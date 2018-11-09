from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from project_app import html_hepler
from project_app.models import Project
from project_app.forms import ProjectForm

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
    '''
    首页跳转，判断参数是否为空，如果为空，查询所有数据，否则查询匹配数据
    '''
    page = request.GET.get('page')

    page = try_int(page, 1)

    count = Project.objects.all().count()

    pageObj = html_hepler.PageInfo(page, count)

    content = request.POST.get('search_project')

    if content is not None:
        project_data = Project.objects.filter(
                title__contains=content)
    else:
        project_data = Project.objects.all()[pageObj.start:pageObj.end]

    #project_data = Project.objects.all()[pageObj.start:pageObj.end]

    page_string = html_hepler.Pager(page, pageObj.all_page_count)
    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "project_manage.html", {"user": username,"project_data":project_data,
                                                   "page": page_string,"type":"list"})

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







