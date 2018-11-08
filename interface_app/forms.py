from django import forms
from interface_app.models import TestCase

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        # exclude哪些字段除外，显示哪些字段用fields
        fields = ['module']
