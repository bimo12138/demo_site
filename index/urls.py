"""
@author:      13716
@date-time:   2019/5/16-22:13
@ide:         PyCharm
@name:        urls.py
"""

from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path("", views.IndexHander.as_view(), name="index"),
    path("welcome", views.WelcomeHandler.as_view(), name="co_introduction"),
    path("login", views.LoginHandler.as_view(), name="login"),
    path("logout", views.LogoutHandler.as_view(), name="logout"),
    path("register", views.RegisterHandler.as_view(), name="register"),
    path("subsidiary/<str:subsidiary_name>", views.SubsidiaryHandler.as_view(), name="subsidiary_detail")
]
