from django.shortcuts import render,redirect,HttpResponse,render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from user_app.models import projectTable
from django.db.models import Q
import json
from datetime import datetime,date
# Create your views here.

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


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
    project_data = projectTable.objects.all()
    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "project_manage.html", {"user": username,"project_data":project_data})


#退出登录
@login_required
def logout1(request):
    #自动清除session
    logout(request)
    return HttpResponseRedirect("/accounts/login/")

@login_required
def project_model(request):
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
    id = request.GET.get('id')
    projectTable.objects.filter(id=id).delete()
    return HttpResponseRedirect('/project_manage/')

#项目管理-编辑
@login_required
def project_edit(request):
    id = request.GET.get('id')
    project_data = projectTable.objects.filter(id = id).first()
    return render(request, "project_model_edit.html", {"project_data":project_data})

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
@login_required
def project_search(request):
    username = request.session.get('user1', '')
    content = request.POST.get('search_project')
    print(content)
    #content="11"
    project_data = projectTable.objects.filter(
                title__contains=content)

    return render(request, "project_manage.html", {"username":username,"project_data": project_data})






