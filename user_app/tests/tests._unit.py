from django.test import TestCase,Client
from django.contrib.auth.models import User
# Create your tests here.


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create_user("test01","test01@mail.com","test01")
        self.client = Client()

    def test_create_user_data(self):
        '''测试创建用户表数据'''
        User.objects.create_user("test02","test02@mail.com","test02")
        user = User.objects.get(username = "test02")
        self.assertEqual(user.email,"test02@mail.com")


    def test_find_user_data(self):
        '''测试查询用户表数据'''
        user = User.objects.get(username = "test01")
        print(user.email)
        self.assertEqual(user.email,"test01@mail.com")
        #print(user.username)
        #print(user.password)

    def test_update_user_data(self):
        user = User.objects.get(username="test01")
        User.objects.filter(username=user.username).update(username='test03',email='test03@mail.com')
        user1 = User.objects.get(username="test03")
        self.assertEqual(user1.email, "test03@mail.com")

    def test_delete_user_data(self):
        User.objects.get(username="test01").delete()

        user = User.objects.all()

        self.assertEqual(len(user),0)

    '''以下是views层的测试用例'''

    def test_index_html(self):
        '''测试首页'''
        response = self.client.get("/")

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"index.html")

    def test_login_null(self):
        '''测试用户名密码为空'''
        login_Data = {"username":"","password":""}
        response = self.client.post("/user/login_action/",data=login_Data)
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码为空",login_html)
        #self.assertTemplateUsed(response, "index.html")

    def test_login_error(self):
        '''测试用户名密码错误'''
        login_Data = {"username": "111", "password": "111"}
        response = self.client.post("/user/login_action/", data=login_Data)
        login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 200)
        self.assertIn("用户名或密码错误", login_html)
        # self.assertTemplateUsed(response, "index.html")

    def test_login_success(self):
        '''测试登录成功'''
        login_Data = {"username": "test01", "password": "test01"}
        response = self.client.post("/user/login_action/", data=login_Data)
        #login_html = response.content.decode("utf-8")
        self.assertEqual(response.status_code, 302)

    def test_login_success(self):
        '''测试退出成功'''
        response = self.client.post("/user/logout/")

        self.assertEqual(response.status_code, 302)
