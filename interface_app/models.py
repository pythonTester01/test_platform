from django.db import models
from project_app.models import Project,Model

# Create your models here.
class TestCase(models.Model):
    #测试用例表
    #project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module = models.ForeignKey(Model, on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=50,default="")
    url = models.CharField("URL",max_length=50,default="")
    req_methed = models.CharField("方法", max_length=50,default="")
    req_type = models.CharField("参数类型", max_length=50,default="")
    req_header = models.TextField("HEADER",default="")
    req_para = models.TextField("参数",default="")
    response_assert = models.TextField("验证",default="")
    creator = models.TextField("创建人",default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name

class TestTask(models.Model):
    #测试任务表
    name = models.CharField("名称",max_length=50,default="")
    describe = models.TextField("描述", default="")
    cases = models.TextField("用例", default="")
    status = models.IntegerField("状态",default=0)
    #run_time =  models.DateTimeField("运行时间")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    #测试结果表
    name = models.CharField("名称",max_length=100,blank=False,default="")
    task = models.ForeignKey(TestTask, on_delete=models.CASCADE)
    error = models.ImageField("错误用例")
    failures = models.ImageField("失败用例")
    skipped =  models.ImageField("跳过用例")
    tests = models.ImageField("总用例数")
    run_time = models.FloatField("运行时长")
    result = models.TextField("详细",default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name