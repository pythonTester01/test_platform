1.创建project_app,添加urls.py

2.使用include整合不同app的urls

3.在project_app添加models，admin代码，将project相关代码移至创建project_app下vies.py文件中，并添加返回属性type=list|add|edit。

4.整合HTML，将新增页面和编辑页面整合至project_manage中，使用{% if type=""%}将三个页面整合为一个。

