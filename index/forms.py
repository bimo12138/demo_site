"""
@author:      13716
@date-time:   2019/5/17-22:32
@ide:         PyCharm
@name:        forms.py
"""

from django import forms


class UserLogin(forms.Form):

    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=30)


class UserRegister(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=30)
    password_check = forms.CharField(label="复核密码", max_length=30)