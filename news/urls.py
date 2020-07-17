"""
@author:      13716
@date-time:   2019/5/19-10:58
@ide:         PyCharm
@name:        urls.py
"""

from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path("", views.NewsIndexHandler.as_view(), name="index"),
    path("location", views.NewsLocationHandler.as_view(), name="location"),
    path("videos", views.VideoCenterHandler.as_view(), name="videos"),
    path("industry", views.IndustryHandler.as_view(), name="industry"),
    path("<int:news_id>/", views.NewsDetailHandler.as_view(), name="news_detail")
]