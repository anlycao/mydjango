from django.urls import path
from .import views

urlpatterns=[
    path('login.html',views.LoginView,name='login'),
    path('register.html',views.registerView,name='register'),
    path('setpassword.html',views.setpasswordView,name='setpassword'),
    path('logout.html',views.logoutView,name='logout'),]

