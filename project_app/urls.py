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

from project_app.views import module_views
from project_app.views import project_views

urlpatterns = [
     path("project_manage/", project_views.project_manage),
     path("module_manage/", module_views.module_manage),
     #path("project_model/", views.project_model),
     #path("project_model_add/", views.project_model_add),
     #path("project_model_del/", views.project_model_del),
     #path("project_model_update/", views.project_model_update),
     path("add_project/", project_views.add_project),
     path("edit_project/<int:pid>/", project_views.edit_project),
     path("del_project/", project_views.del_project),
     path("add_module/", module_views.add_module),
     path("edit_module/<int:pid>/", module_views.edit_module),
     path("del_module/", module_views.del_module),

]
