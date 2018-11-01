from django.shortcuts import render

# Create your views here.

def case_manage(request):

    if request.method == "GET":
        return render(request,"case_manage.html",{"type":"list"})
    else:
        return "404"


def api_debug(request):
    '''创建调试接口'''
    return render(request, "api_debug.html", {"type": "api_debug"})