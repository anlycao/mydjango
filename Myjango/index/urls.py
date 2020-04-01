
from django.urls import path # 导入url编写模块
from index import views


urlpatterns=[
    path('',views.index)
]