from django.test import TestCase,Client
from django.contrib.auth.models import User
from project_app.models import Model
from project_app.models import Project
# Create your tests here.

class ModleTest(TestCase):

    def setUp(self):
        User.objects.create_user("test01","test01@mail.com","test01")
        project = Project.objects.create(title="test01",describe="test01")
        Model.objects.create(name = "teeee",describe="test01",project=project)
        self.client = Client()
        login_Data = {"username": "test01", "password": "test01"}
        self.client.post("/user/login_action/", data=login_Data)

    def test_module_find(self):
        '''模块列表'''
        response = self.client.post("/manage/module_manage/")
        porject_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn('teeee', porject_html)

    def test_module_add(self):
        '''添加模块'''
        data = {"name": "test", "describe": "test", "project":1}
        self.client.post("/manage/add_module/", data=data)
        response = self.client.post("/manage/module_manage/")
        porject_html = response.content.decode("utf-8")

        #print(porject_html)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test',porject_html)

    def test_module_edit(self):
        '''编辑模块'''
        data = {"name": "test001", "describe": "test001", "project": 1}
        self.client.post("/manage/edit_module/1/", data=data)
        response = self.client.post("/manage/module_manage/")
        porject_html = response.content.decode("utf-8")

        #print(porject_html)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test001', porject_html)


    def test_module_delete(self):
        '''删除模块'''
        data = {"id":"1", "project": 1}
        self.client.post("/manage/del_module/", data=data)
        response = self.client.post("/manage/module_manage/")
        porject_html = response.content.decode("utf-8")
        moduel = Model.objects.filter(id=1)
        # print(porject_html)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(moduel), 0)

    '''以下是model层的单元测试'''

    def test_find_module(self):
        '''model查询'''
        data = Model.objects.get(name="teeee")
        self.assertEqual(data.name, 'teeee')


    def test_add_module(self):
        '''model添加'''
        project = Project.objects.get(id="1")
        Model.objects.create(name="zhangsan",describe="test001", project=project)
        model = Model.objects.get(name="zhangsan")
        self.assertEqual("zhangsan", model.name)


    def test_module_update(self):
        '''model更新'''
        project = Project.objects.get(id="1")
        Model.objects.filter(name="teeee").update(name="test02", describe="test001", project=project)
        model = Model.objects.get(name="test02")
        self.assertEqual("test02", model.name)

    def test_module_delete(self):
        '''model删除'''
        Model.objects.get(name="teeee").delete()
        model = Model.objects.all()
        #model = Model.objects.get(name="test02")
        self.assertEqual(len(model), 0)
