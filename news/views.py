from django.shortcuts import render, redirect, reverse
from django.views import View
from index.models import News, Classifies, Subsidiary, NewsImage, Video


class NewsIndexHandler(View):

    def get(self, request):
        classify_id = Classifies.objects.get(classify="集团动态")
        news = News.objects.filter(classify_id=classify_id)
        context = {
            "user": request.user,
            "news": news
        }
        return render(request, "news_index.html", context=context)


class NewsActionHandler(View):

    def get(self, request):
        pass


class NewsDetailHandler(View):

    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        context = {
            "user": request.user,
            "news": news
        }
        return render(request, "news_detail.html", context=context)


class NewsLocationHandler(View):
    def get(self, request):
        news_id = Classifies.objects.get(classify="本地要闻")
        news = News.objects.filter(classify_id=news_id)
        context = {
            "locations": news,
            "user": request.user
        }
        return render(request, "news_location.html", context=context)


class VideoCenterHandler(View):
    def get(self, request):
        videos = Video.objects.all()
        context = {
            "videos": videos,
            "user": request.user
        }
        return render(request, "news_videos.html", context=context)


class IndustryHandler(View):
    def get(self, request):
        news_id = Classifies.objects.get(classify="通知公告")
        industries = News.objects.filter(classify_id=news_id)
        context = {
            "industries": industries,
            "user": request.user
        }
        return render(request, "news_industry.html", context=context)