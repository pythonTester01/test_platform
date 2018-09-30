from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from user_app.models import projectTable

# Create your views here.

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

@login_required
def project_model_add(request,*args,**kwargs):
    print("====")
    title = request.POST.get('title')
    a = request.POST.get('a')
    b = request.POST.get('b')
    projectTable.objects.create(title=title, a=a, b=b)
    return HttpResponseRedirect('/project_manage/')

def project_del(request):
    id = request.GET.get('id')
    projectTable.objects.filter(id=id).delete()
    return HttpResponseRedirect('/project_manage/')

def project_edit(request):
    id = request.GET.get('id')
    project_data = projectTable.objects.filter(id = id).first()
    return render(request, "project_model_edit.html", {"project_data":project_data})

def project_update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        title = request.POST.get('title')
        a = request.POST.get('a')
        b = request.POST.get('b')
        projectTable.objects.filter(id=id).update(title=title, a=a, b=b)
        return HttpResponseRedirect('/project_manage/')



