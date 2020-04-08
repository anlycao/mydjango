
from django.urls import path, re_path  # 导入url编写模块
from . import views


urlpatterns=[
    path('',views.index),
    #带有字符类型、整型的url
    #path('<year>/<int:month>/<slug:day>',views.mydate),    #http://127.0.0.1/2020/05/01
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.mydate),#http://127.0.0.1/2016/15/21.html
    #re_path('(?P<year>[0-9]{4}).html', views.myyear,name='myyear'),
    re_path('dict/(?P<year>[0-9]{4}).html', views.myyear_dict, {'month':'05'},name='myyear_dict'),
    path('download.html',views.download),
    path('/',views.index),
    path('data.html',views.data),
    #path('login.html',views.login),
    #path('/',views.ProductList.as_view()),
    path('create/',views.create),
    path('update/',views.updatel),
    path('select/',views.select),
    path('delete/',views.delete),
    path('form.html',views.form)

]