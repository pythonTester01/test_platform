from django.contrib import admin
from user_app.models import Project,Model
# Register your models here.
# 映射自己创建的表,后台显示下列字段
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ["title","describe","status","create_time","id"]
#
# class ModelAdmin(admin.ModelAdmin):
#     list_display = ["name","describe","create_time","project","id"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'describe', 'status', 'create_time', 'id']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project', 'id']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Model,ModuleAdmin)
