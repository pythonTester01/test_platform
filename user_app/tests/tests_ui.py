from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project

class loginTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def setUp(self):
        """初始化数据"""
        User.objects.create_user("test01", "test01@mail.com", "test01")
        Project.objects.create(title="测试平台项目", describe="描述")

    def test_login_null(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_name("username").send_keys("")
        self.driver.find_element_by_name("password").send_keys("")
        self.driver.find_element_by_class_name("btn").click()

        text = self.driver.find_element_by_id("error").text

        self.assertIn(text,"用户名或密码为空")

    def test_login_error(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_name("username").send_keys("111")
        self.driver.find_element_by_name("password").send_keys("111")
        self.driver.find_element_by_class_name("btn").click()

        text = self.driver.find_element_by_id("error").text

        self.assertIn(text, "用户名或密码错误")

    def test_login_success(self):
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        self.driver.find_element_by_name("username").send_keys("test01")
        self.driver.find_element_by_name("password").send_keys("test01")
        self.driver.find_element_by_class_name("btn").click()

        text = self.driver.find_element_by_class_name("brand").text

        self.assertIn(text, "Admin Panel")