from django.db import models
from django.contrib.auth.models import User

"""修改模型后需要保存更新数据库
python manage.py makemigrations
python manage.py migrate
建议备份数据库（简单复制备份db.sqlite3即可）
"""


class Dmc(models.Model):  # Create your models here.
    title = models.CharField(max_length=30)  # 标题字段
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    is_deleted = models.BooleanField(default=False)
    readed_num=models.IntegerField(default=0)

    def __str__(self):
        """使后台管理显示名称http://127.0.0.1:8000/admin/dmc/dmc/"""
        return '<Dmc:%s>' % self.title
