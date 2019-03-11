from django.contrib import admin
from .models import Dmc


# Register your models here.注册模型
@admin.register(Dmc)  # 或者用dmin.site.register(Dmc, DmcAdmin)
class DmcAdmin(admin.ModelAdmin):  # 用于定制管理界面
    list_display = ('id', 'title', 'content', 'author', 'is_deleted','created_time',
                    'last_update_time')  # 定制管理界面http://127.0.0.1:8000/admin/dmc/dmc/?o=-1
    ordering = ('id',)  # 单元素元组必须带括号，正负表示是否添加-号
