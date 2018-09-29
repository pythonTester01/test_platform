<h2>完善登录退出、加入cookie、本地CSS文件引用及首页样式开发</h2>
<ul>
<li>修改模板目录templates/ 移动到项目跟目录下面（方便维护）。</li>
<li>创建静态文件目录 static/ 引用本地资源文件（不依赖于网络样式）。</li>
<li>利用浏览器cookie 记录用户名，并显示在登录成功页面。再改为session </li>
<li>利用bootstrap 制作登录成功之后的页面，设计主要菜单。</li>
<li>添加退出功能。
</ul>
1.修改模板目录, test_platform/settings

<pre><code>
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [] //原先
        'DIRS': [os.path.join(BASE_DIR, 'templates')],//修改后
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
</pre></code>

2.创建静态文件目录, test_platform/settings

<pre><code>
STATICFILES_DIRS = [
    # ...
    os.path.join(BASE_DIR, 'static'),
]
</pre></code>

3.下载Bootstrap JS/CSS/Fonts文件到本地 https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip

4.引用本地css文件

<pre><code>
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static "css/signin.css" %}">
</pre></code>

5.添加cookie功能 user_app/views

<pre><code>
def login_action(request):
        ...
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/project_manage/')
            response.set_cookie('user', username, 3600)  # 添加浏览器 cookie
            return response
        ...

def project_manage(request):
    username = request.COOKIES.get('user', '')
    return render(request, 'project_manage.html', {"username": username})

</pre></code>

6.把cookie改为session

<pre><code>
修改.../sign/views.py 文件， 在 login_action 函数中， 将：
response.set_cookie('user', username, 3600)

替换为：
request.session['user'] = username # 将 session 信息记录到浏览器

在 project_manage 函数中， 将：

username = request.COOKIES.get('user', '')

替换为：
username = request.session.get('user', '') # 读取浏览器 session
</pre></code>

7.根据下载Bootstrap 提供的模板开发首页模块 https://v3.bootcss.com/examples/dashboard/

8.完成退出功能

<pre><code>
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/')
    return response
</pre></code>

9.访问系统接口加上登录认证

<pre><code>
def login_action(request):
        ...
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) // 记住用户登录状态
        ...


@login_required // from django.contrib.auth.decorators import login_required
def project_manage(request):
    username = request.session.get('user', '')  # 读取浏览器 session
    return render(request, 'project_manage.html', {"username": username})
</pre></code>