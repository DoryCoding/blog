# coding:utf-8
from django.conf.urls import url

from . import views

# 命名空间
app_name = 'blog'


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='detail'),
]