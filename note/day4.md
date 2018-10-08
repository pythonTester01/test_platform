<h2>尝试完成项目管理功能</h2>
<ul>
<li>项目列表展示</li>
<li>添加</li>
<li>编辑</li>
<li>删除</li>
</ul>

1.新增HTML project_model_add.html

2.添加页面静态公共模板 nav，使project_manage.html project_model_add.html 使用公共页面nav.html

3.新增功能代码

<pre><code>
@login_required
def project_model_add(request,*args,**kwargs):
    print("====")
    title = request.POST.get('title')
    a = request.POST.get('a')
    b = request.POST.get('b')
    projectTable.objects.create(title=title, a=a, b=b)
    return HttpResponseRedirect('/project_manage/')
</pre></code>

4.编辑功能代码

<pre><code>
@login_required
def project_model(request):
    '''
    判断id是否为空，如果空，跳转添加页面，否则回显数据，变为修改页面。
    '''
    id = request.GET.get('id')
    print(id)
    if id is not None:
        project_data = projectTable.objects.filter(id=id).first()
        return render(request, "project_model_add.html",{"project_data":project_data})
    else:
        return render(request, "project_model_add.html")
</pre></code>

5.删除功能

<pre><code>
#项目管理-删除（根据id删除）
@login_required
def project_del(request):
    id = request.POST.get('id')
    projectTable.objects.filter(id=id).delete()
    #return HttpResponseRedirect('/project_manage/')
    return HttpResponse('1')
</pre></code>

6.更新功能

<pre><code>
@login_required
def project_update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        a = request.POST.get('a')
        b = request.POST.get('b')
        projectTable.objects.filter(id=id).update(title=title, a=a, b=b)
        return HttpResponseRedirect('/project_manage/')
</pre></code>

7.添加分页公共方法html_hepler.py

8.添加参数默认为int方法

<pre><code>
'''
默认值转换为int
'''
def try_int(arg,default):
    try:
        arg = int(arg)
    except Exception as e:
        arg = default
    return arg
</pre></code>

9.修改首页查询方法，增加分页

<pre><code>
@login_required #判断用户是否登录
def project_manage(request):
    '''
    1.首页跳转，判断参数是否为空，如果为空，查询所有数据，否则查询匹配数据。
    2.使用分页方法，返回前端页面。
    '''
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
</pre></code>
