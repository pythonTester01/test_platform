<h2>使用数据库里的用户进行登录</h2>

1.表单为post请求时，解决csrf问题，修改test_platform/settings

<pre><code>
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
</code></pre>

2.用户名和密码传入默认参数，默认参数为空

<pre><code>
username = request.POST.get("username")
username = request.POST.get("username", "")
</code></pre>

3.创建超级管理员账户

<pre><code>
python3 manage.py createsuperuser
</pre></code>

4.生成数据库文件,使用sqlite打开

<pre><code>
python3 manage.py migrate
</pre></code>

5.浏览器访问后台 127.0.0.1:8000/admin

6.views.py 导入auth

<pre><code>
from django.contrib import auth
username = request.POST.get("username", "")
password = request.POST.get("password", "")
user = auth.authenticate(username=username, password=password)
if user is not None:
    auth.login(request, user)
    return render(request, 'project_manage.html')
</pre></code>

7.使用bootstarp优化登录页面，注意点:css的问题,查看原网页使用的css

<link href="https://v3.bootcss.com/examples/signin/signin.css" rel="stylesheet">
