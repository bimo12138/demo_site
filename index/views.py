from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import News, Classifies, Subsidiary, NewsImage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserLogin, UserRegister
from django.contrib.auth.models import User
from utils import resultful


class IndexHander(View):

    def get(self, request):
        news_image = NewsImage.objects.all()
        classify_id = Classifies.objects.get(classify="集团动态")
        news = News.objects.filter(classify_id=classify_id)[:4]
        classify_id_2 = Classifies.objects.get(classify="通知公告")
        actions = News.objects.filter(classify_id=classify_id_2)[:4]
        classify_id_3 = Classifies.objects.get(classify="本地要闻")
        industry_news = News.objects.filter(classify_id=classify_id_3)[:4]
        context = {
            "user": request.user,
            "news_images": news_image,
            "news": news,
            "actions": actions,
            "industry_news": industry_news
        }
        return render(request, "index.html", context=context)


class WelcomeHandler(View):

    def get(self, request):
        classify_id = Classifies.objects.get(classify="企业简介")
        try:
            co_introduction = News.objects.filter(classify_id=classify_id)[0]
            try:
                classify_id = Classifies.objects.get(classify="组织架构")
                organization = News.objects.filter(classify_id=classify_id)[0]
                context = {
                    "co_introduction": co_introduction,
                    "user": request.user,
                    "organization": organization,
                }
                return render(request, "co_introduction.html", context=context)
            except:
                context = {
                    "co_introduction": co_introduction,
                    "user": request.user,
                    "organization": None,
                }
                return render(request, "co_introduction.html", context=context)
        except:
            try:
                classify_id = Classifies.objects.get(classify="组织架构")
                organization = News.objects.filter(classify_id=classify_id)[0]
                context = {
                    "co_introduction": None,
                    "user": request.user,
                    "organization": organization,
                }
                return render(request, "co_introduction.html", context=context)
            except:
                context = {
                    "co_introduction": None,
                    "user": request.user,
                    "organization": None,
                }
                return render(request, "co_introduction.html", context=context)


class LoginHandler(View):

    def get(self, request):

        return render(request, "login.html")

    def post(self, request):
        message = UserLogin(request.POST)
        if message.is_valid():
            username = message.cleaned_data['username']
            password = message.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return resultful.result(message="登陆成功！")
            else:
                return resultful.params_error(message="账户或密码错误！请重新输入！")
        else:
            return resultful.server_error(message="表单验证失败！")


class RegisterHandler(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        message = UserRegister(request.POST)
        if message.is_valid():
            username = message.cleaned_data['username']
            password = message.cleaned_data['password']
            password_check = message.cleaned_data['password_check']
            if password == password_check:
                if User.objects.filter(username=username):
                    return resultful.params_error(message="该用户名已经被占用！")
                else:
                    user = User.objects.create_user(username=username)
                    user.set_password(password)
                    user.save()
                    log_user = authenticate(request, username=username, password=password)
                    login(request, log_user)
                    return resultful.result(message="注册成功~！~")
            else:
                return resultful.params_error("两次密码输入不一致！")
        else:
            return resultful.server_error(message="表单验证错误！请重试！")


class LogoutHandler(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("index:index"))


class SubsidiaryHandler(View):
    def get(self, request, subsidiary_name):
        subsidiary = Subsidiary.objects.get(subsidiary_name=subsidiary_name)
        context = {
            "user": request.user,
            "subsidiary": subsidiary
        }
        return render(request, "index_subsidiary.html", context=context)