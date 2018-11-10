from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from common.page_help import page
from project_app.forms import ModuleForm
from project_app.models import Model

# Create your views here.

@login_required #判断用户是否登录
def module_manage(request):
    '''模块列表页'''

    module_data = Model.objects.all().order_by("-create_time")

    contacts = page(request,module_data)

    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "module_manage.html", {"contacts":contacts,"type":"list","username":username})

def search_module(request):
    '''模块搜索功能'''
    if request.method == "GET":
        search_module = request.GET.get("search_module", "")
        module_data = Model.objects.filter(name__icontains=search_module)
        contacts = page(request, module_data)
        return render(request, "case_manage.html", {"type": "list", "contacts": contacts, "search_module": search_module})
    else:
        return "404"


@login_required
def add_module(request):
    '''添加模块'''
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            project = form.cleaned_data["project"]
            Model.objects.create(name=name, describe=describe, project=project)
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        form = ModuleForm()
    return render(request, "module_manage.html", {"type": "add","form":form})


@login_required
def edit_module(request,pid):
    '''
    编辑模块功能
    '''
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            project = form.cleaned_data["project"]
            Model.objects.filter(id=pid).update(name=name, describe=describe,project=project)
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        if pid:
            form = ModuleForm(instance = Model.objects.filter(id=pid).first())
        #project_data = Project.objects.filter(id=pid).first()

    return render(request, "module_manage.html", { "type": "edit","form":form,"id":pid})

@login_required
def del_module(request):
    '''模块删除'''
    id = request.POST.get('id')
    Model.objects.get(id=id).delete()
    return HttpResponse('1')







