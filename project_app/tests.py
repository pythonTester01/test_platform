from django.test import TestCase,Client
from django.contrib.auth.models import User
from project_app.models import Project
# Create your tests here.

class ProjectTest(TestCase):

    def setUp(self):
        User.objects.create_user("test01","test01@mail.com","test01")
        Project.objects.create(title="test01",describe="test01")
        self.client = Client()
        login_Data = {"username": "test01", "password": "test01"}
        self.client.post("/user/login_action/", data=login_Data)
        print("1")

    def test_project_list(self):
        '''项目管理列表'''
        response = self.client.post("/manage/project_manage/")
        porject_html = response.content.decode("utf-8")
        self.assertIn("安全退出",porject_html)
        self.assertIn("test01",porject_html)
        self.assertEqual(response.status_code, 200)
        #print(porject_html)
        print("2")

    def test_project_add(self):
        '''添加项目'''
        data = {"pid":"999","title": "test02", "describe": "test02","status":"True"}
        self.client.post("/manage/add_project/",data=data)
        response = self.client.post("/manage/project_manage/")
        porject_html = response.content.decode("utf-8")

        #print(porject_html)
        #print("============")
        self.assertIn("test02", porject_html)
        self.assertEqual(response.status_code, 200)
        print("3")


        def test_project_edit(self):
            '''编辑项目'''

        data = {"title": "test03", "describe": "test03", "status": "False"}
        self.client.post("/manage/edit_project/1/", data=data)
        response = self.client.post("/manage/project_manage/")
        porject_html = response.content.decode("utf-8")

        #print(porject_html)
        self.assertIn("test03", porject_html)
        self.assertEqual(response.status_code, 200)
        print("4")

    def test_project_delete(self):
        '''删除项目'''
        data = {"id":"1"}
        self.client.post("/manage/del_project/",data=data)
        response = self.client.post("/manage/project_manage/")
        porject_html = response.content.decode("utf-8")

        #print(porject_html)
        self.assertNotIn(porject_html,"test01" )
        self.assertEqual(response.status_code, 200)
        print("5")

    '''以下是models层的单元测试'''

    def test_find_project(self):
        project = Project.objects.get(title = "test01")
        self.assertEqual("test01",project.title)

    def test_add_project(self):
        Project.objects.create(title="test02",describe="aaa")
        project = Project.objects.get(title="test02")
        self.assertEqual("test02", project.title)

    def test_update_project(self):
        project = Project.objects.get(title = "test01")
        Project.objects.filter(title=project.title).update(title="test03", describe="333aaa")
        project = Project.objects.get(title="test03")
        self.assertEqual("test03", project.title)

    def test_delete_project(self):
        Project.objects.get(title="test01").delete()
        project = Project.objects.all()
        self.assertEqual(len(project), 0)