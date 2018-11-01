from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from project_app import html_hepler
from project_app.models import Model
from project_app.forms import ProjectForm,ModuleForm

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
def module_manage(request):
    '''
    首页跳转，判断参数是否为空，如果为空，查询所有数据，否则查询匹配数据
    '''
    page = request.GET.get('page')

    page = try_int(page, 1)

    count = Model.objects.all().count()

    pageObj = html_hepler.PageInfo(page, count)

    content = request.POST.get('search_project')

    if content is not None:
        project_data = Model.objects.filter(
                name__contains=content)
    else:
        project_data = Model.objects.all()[pageObj.start:pageObj.end]

    #project_data = Project.objects.all()[pageObj.start:pageObj.end]

    page_string = html_hepler.Pager(page, pageObj.all_page_count)
    username = request.session.get('user1', '')  # 读取浏览器 session
    return render(request, "module_manage.html", {"user": username,"project_data":project_data,
                                                   "page": page_string,"type":"list"})


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







