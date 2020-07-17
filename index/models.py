from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Classifies(models.Model):
    id = models.AutoField(primary_key=True)
    classify = models.CharField(max_length=20)

    class Meta:
        db_table = "classifies"
        verbose_name = "新闻分类"

    def __str__(self):
        return "id : {}\n classify: {}".format(self.id, self.classify)


class News(models.Model):
    title = models.CharField(max_length=100)
    classify = models.ForeignKey(Classifies, on_delete=models.SET_NULL, null=True)
    content = RichTextField()
    upload_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
        ordering = ['upload_time']
        verbose_name = "新闻"

    def __str__(self):
        return self.title


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="image")

    class Meta:
        db_table = "image"
        verbose_name = "图片"

    def __str__(self):
        return "http://192.168.155.41:8000/media/{}".format(self.img.name)


class NewsImage(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to="image")
    img_desc = models.TextField()

    class Meta:
        db_table = "news_images"
        verbose_name = "新闻图片"

    def __str__(self):
        return "{} \t http://192.168.155.41:8000/media/{}".format(self.img_desc, self.img.name)


class Goods(models.Model):

    good_id = models.AutoField(primary_key=True)
    good_name = models.CharField(max_length=100)
    good_price = models.DecimalField(max_length=5, max_digits=4, decimal_places=2)
    good_desc = RichTextField()
    good_producer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    good_img = models.URLField(max_length=100)

    class Meta:
        db_table = "goods"
        verbose_name = "商品"

    def __str__(self):

        return self.good_name


class Subsidiary(models.Model):
    id = models.AutoField(primary_key=True)
    subsidiary_name = models.CharField(max_length=20)
    subsidiary_desc = RichTextField()

    class Meta:
        db_table = "subsidiaries"
        verbose_name = "子公司"

    def __str__(self):

        return self.subsidiary_name


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    video = models.FileField(upload_to="videos")
    upload_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "video"
        verbose_name = "视频"

    def __str__(self):
        return "http://192.168.155.41:8000/media/{}".format(self.video.name)

