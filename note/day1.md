
<h3>主流程</h3>
<ol>
<li>安装python3.6、django2.1</li>
</ol>
<pre><code>pip install django==2.1
</code></pre>
<ol start="2">
<li>创建项目</li>
</ol>
<pre><code>python3 manage.py startproject test_platform
</code></pre>
<ol start="3">
<li>创建APP</li>
</ol>
<pre><code>python3 manage.py startapp user_app
</code></pre>
<ol start="4">
<li>打开test_platform/settings 注册APP</li>
</ol>
<pre><code>INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_app',
]
</code></pre>
<ol start="5">
<li>认识django MTV 模式</li>
</ol>
<ul>
<li>M 代表模型(Model),即数据存取层。 该层处理与数据相关的所有事务： 如何存取、 如何验证有效</li>
<li>T 代表模板(Template),即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。</li>
<li>V 代表视图(View),即业务逻辑层。</li>
</ul>
<ol start="6">
<li>
<p>在test_platform/urls 下面添加路由，在APP下面新建templates，存放html文件，views编写逻辑</p>
</li>
<li>
<p>未使用models.py ，实现假登录业务</p>
</li>
<li>
<p>启动项目</p>
</li>
</ol>
<pre><code>python3 manage.py runserver
</code></pre>
