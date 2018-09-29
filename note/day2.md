使用数据库里的用户进行登录
表单为post请求时，解决csrf问题，修改test_platform/settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
用户名和密码传入默认参数，默认参数为空
username = request.POST.get("username")
username = request.POST.get("username", "")
创建超级管理员账户
python3 manage.py createsuperuser
生成数据库文件,使用sqlite打开
python3 manage.py migrate
浏览器访问后台 127.0.0.1:8000/admin

views.py 导入auth

from django.contrib import auth

username = request.POST.get("username", "")
password = request.POST.get("password", "")
user = auth.authenticate(username=username, password=password)
if user is not None:
    auth.login(request, user)
    return render(request, 'project_manage.html')
使用bootstarp优化登录页面，注意点:css的问题,查看原网页使用的css
<link href="https://v3.bootcss.com/examples/signin/signin.css" rel="stylesheet">