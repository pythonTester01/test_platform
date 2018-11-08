from django.contrib import admin
from interface_app.models import TestCase
# Register your models here.

class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['module', 'name',
                    'url', 'req_methed', 'req_type',
                    'req_header', 'req_para', 'response_assert',
                    'creator', 'create_time']

admin.site.register(TestCase, TestCaseAdmin)

