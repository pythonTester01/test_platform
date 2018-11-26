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

from interface_app import views


urlpatterns = [
     path("case_manage/", views.case_manage),
     path("api_debug/", views.api_debug),
     path("add_case/", views.add_case),
     path("save_case/", views.save_case),
     path("del_case/", views.del_case),
     path("edit_case/<int:mid>/", views.edit_case),
     path("search_case/", views.search_case),
     path("get_case_info/", views.get_case_info),
     path("get_project_list/", views.get_project_list),
     path("update_case/", views.update_case),
     path("api_assert/", views.api_assert),


]
