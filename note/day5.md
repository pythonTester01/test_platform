1.将model注册到django后台
<pre><code>
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'describe', 'status', 'create_time', 'id']


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project', 'id']

admin.site.register(Project,ProjectAdmin)
admin.site.register(Model,ModuleAdmin)
</pre></code>

2.修改数据库表字段，添加model表，使其与project表关联

3.修改登录后查询项目代码

<pre><code>
前端代码
<thead>
    <tr>
        <th>序号</th>
        <th>项目名称</th>
        <th>状态</th>
        <th>描述</th>
        <th>创建时间</th>
        <th>操作</th>
    </tr>
</thead>
<tbody>
{% for data in project_data %}
    <tr class="gradeU">
        <td>{{forloop.counter }}</td>
        <td>{{data.title}}</td>
        <td>{{data.status}}</td>
        <td class="center">{{data.describe}}</td>
        <td class="center">{{data.create_time |date:"Y-m-d H:i"}}</td>
        <td class="center" style="width: 60px;">
            <a onclick="del_id()"><i class="icon-remove"><input type="hidden" id="del_id" value={{ data.id }}></i></a>
            &nbsp;&nbsp;&nbsp;
            <a href="/project_model/?id={{ data.id }}"><i class="icon-pencil"></i></a>
        </td>
    </tr>
{% endfor %}
</tbody>
</pre></code>
