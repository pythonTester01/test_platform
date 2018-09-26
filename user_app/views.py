from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login

# Create your views here.

#登录首页
def index(request):
    return  render(request,"index.html")

#登录->使用django提供的登录方法
def login_action(request):
    if request.method =="POST":
         username = request.POST.get("username","")
         password = request.POST.get("password","")

    if username =="" or password =="":
        return render(request,"index.html",{"error":"用户名或密码为空"})
    else:
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request, "project_manage.html")
        else:
            return render(request, "index.html", {"error": "用户名或密码错误"})
    # if username == "" and password == "":
    #     return render(request,"project_manage.html")
    # else:
    #     return render(request,"index.html",{"error":"用户名或密码错误"})
