from django.db import models
from project_app.models import Project,Model

# Create your models here.
class TestCase(models.Model):
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

    name = models.CharField("名称",max_length=50,default="")
    describe = models.TextField("描述", default="")
    cases = models.TextField("用例", default="")
    status = models.IntegerField("状态",max_length=50,default="")
    #run_time =  models.DateTimeField("运行时间")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name