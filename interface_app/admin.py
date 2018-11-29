from django.contrib import admin
from interface_app.models import TestCase
from interface_app.models import TestTask
# Register your models here.

class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'url', 'req_methed', 'req_type',
                    'req_header', 'req_para', 'response_assert',
                    'creator', 'create_time']

class TestTaskAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'describe', 'cases', 'status',
                    'create_time']

admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestTask, TestTaskAdmin)

