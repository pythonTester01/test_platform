from django.shortcuts import render,redirect,HttpResponse,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from user_app.models import projectTable
from user_app import html_hepler
import json
from datetime import datetime,date
# Create your views here.

def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception as e:
        arg = default
    return arg


#登录首页
def index(request):
    return render(request,"index.html")

#登录->使用django提供的登录方法
def login_action(request):

    if request.method =="POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")

        if username == "" or password == "":
            return render(request,"index.html",{"error":"用户名或密码为空"})
        else:
            user = authenticate(username = username,password = password)

            if user is not None:
                login(request, user)  # 记录用户登录状态
                request.session['user1'] = username
                return HttpResponseRedirect('/project_manage/')
            else:
                return render(request, "index.html", {"error": "用户名或密码错误"})


@login_required #判断用户是否登录
def project_manage(request):
    page = request.GET.get('page')

    page = try_int(page, 1)

    # all_data = models.News.objects.all()
    count = projectTable.objects.all().count()

    pageObj = html_hepler.PageInfo(page, count)
    content = request.POST.get('search_project')
    if content is not None:
        project_data = projectTable.objects.filter(
                title__contains=content)
    else:
        project_data = projectTable.objects.all()[pageObj.start:pageObj.end]

    page_string = html_hepler.Pager(page, pageObj.all_page_count)
    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "project_manage.html", {"user": username,"project_data":project_data,
                                                   "page": page_string})


#退出登录
@login_required
def logout1(request):
    #自动清除session
    logout(request)
    return HttpResponseRedirect("/accounts/login/")

@login_required
def project_model(request):
    id = request.GET.get('id')
    print(id)
    if id is not None:
        project_data = projectTable.objects.filter(id=id).first()
        return render(request, "project_model_add.html",{"project_data":project_data})
    else:
        return render(request, "project_model_add.html")

#项目管理-添加
@login_required
def project_model_add(request,*args,**kwargs):
    print("====")
    title = request.POST.get('title')
    a = request.POST.get('a')
    b = request.POST.get('b')
    projectTable.objects.create(title=title, a=a, b=b)
    return HttpResponseRedirect('/project_manage/')

#项目管理-删除（根据id删除）
@login_required
def project_del(request):
    id = request.POST.get('id')
    projectTable.objects.filter(id=id).delete()
    #return HttpResponseRedirect('/project_manage/')
    return HttpResponse('1')

#项目管理-编辑
# @login_required
# def project_edit(request):
#     id = request.POST.get('id')
#     #print(id)
#     project_data = projectTable.objects.filter(id = id).first()
#     return render(request, "project_model_edit.html", {"project_data":project_data})

#项目管理-更新
@login_required
def project_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        a = request.POST.get('a')
        b = request.POST.get('b')
        projectTable.objects.filter(id=id).update(title=title, a=a, b=b)
        return HttpResponseRedirect('/project_manage/')

#项目管理-搜索
# @login_required
# def project_search(request):
#     username = request.session.get('user1', '')
#     content = request.POST.get('search_project')
#     print(content)
#     #content="11"
#     project_data = projectTable.objects.filter(
#                 title__contains=content)
#
#     return render(request, "project_manage.html", {"username":username,"project_data": project_data})






