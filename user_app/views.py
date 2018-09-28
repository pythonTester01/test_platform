from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


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
    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "project_manage.html", {"user": username})


#退出登录
def logout1(request):
    #自动清除session
    logout(request)
    return HttpResponseRedirect("/accounts/login/")

