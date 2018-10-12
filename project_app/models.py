from django.db import models

# Create your models here.
# 创建数据库表
# 查询类型 F:\Python35\Lib\site-packages\django\db\models\fields\int.py
class Project(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=True)
    create_time = models.DateTimeField("创建时间",auto_now=True)

    def __str__(self):
        return self.title

class Model(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100,blank=False,default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name




