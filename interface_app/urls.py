"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from interface_app.views import testask_view,taks_api
from interface_app.views import testcase_view


urlpatterns = [
     #测试用例
     path("case_manage/", testcase_view.case_manage),
     path("api_debug/", testcase_view.api_debug),
     path("add_case/", testcase_view.add_case),
     path("save_case/", testcase_view.save_case),
     path("del_case/", testcase_view.del_case),
     path("edit_case/<int:mid>/", testcase_view.edit_case),
     path("search_case/", testcase_view.search_case),
     path("get_case_info/", testcase_view.get_case_info),
     path("get_project_list/", testcase_view.get_project_list),
     path("update_case/", testcase_view.update_case),
     path("api_assert/", testcase_view.api_assert),

     #测试任务
     path("task_manage/", testask_view.task_manage),
     path("add_task/", testask_view.add_task),
     path("run_task/<int:tid>", testask_view.run_task),
     path("task_result_list/<int:tid>", testask_view.task_result_list),


     #任务管理-由JS调用
     path("get_case_list/", testcase_view.get_case_list),
     path("save_task_data/", taks_api.save_task_data),
     path("delete_task/", taks_api.delete_task),
     path("save_task_data/", taks_api.save_task_data),
     path("task_result/", taks_api.task_result),

]
