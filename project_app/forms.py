from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    title = forms.CharField(label="项目名称",max_length=100)
    describe = forms.Field(label="描述", required=False,widget=forms.Textarea(attrs={'class':"input-xlarge focused"}))
    status = forms.BooleanField(label="状态",required=False)

    class Meta:
        model = Project
        exclude = ['create_time']
