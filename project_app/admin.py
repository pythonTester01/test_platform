from django.contrib import admin
from project_app.models import Project,Model
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'describe', 'status', 'create_time', 'id']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project', 'id']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Model,ModuleAdmin)