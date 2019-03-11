"""子路由配置"""
from django.urls import path
from .views import Dmc_list, Dmc_detail

urlpatterns = [
    path('<int:dmc_id>', Dmc_detail, name='Dmc_detail'),  # http://127.0.0.1:8000/dmc/
    path('list', Dmc_list, name='Dmc_list'),  # http://127.0.0.1:8000/dmc/list
]
