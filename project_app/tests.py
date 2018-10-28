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

    def test_roject_list(self):
        '''项目管理列表'''
        response = self.client.post("/manage/project_manage/")
        porject_html = response.content.decode("utf-8")
        self.assertIn("安全退出",porject_html)
        self.assertIn("test01",porject_html)
        self.assertEqual(response.status_code, 200)