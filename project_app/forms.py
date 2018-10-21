from django import forms
from .models import Project,Model

class ProjectForm(forms.ModelForm):
    #title = forms.CharField(label="项目名称",max_length=100)
    #describe = forms.Field(label="描述", required=False,widget=forms.Textarea(attrs={'class':"input-xlarge focused"}))
    #status = forms.BooleanField(label="状态",required=False)

    class Meta:
        model = Project
        #exclude哪些字段除外，显示哪些字段用fields
        exclude = ['create_time']
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Model
        # exclude哪些字段除外，显示哪些字段用fields
        exclude = ['create_time']
