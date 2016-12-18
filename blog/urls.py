# coding:utf-8
from django.conf.urls import url

from . import views

# 命名空间
app_name = 'blog'


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<tag>(about))/$',views.about,name='about'),
    url(r'^(?P<tag>[^a][a-zA-Z]+)/$',views.articleByTag,name='articleByTag'),
    url(r'^(?P<article_id>[0-9]+)/star/$',views.star,name='star'),
    url(r'^(?P<article_id>[0-9]+)/$',views.detail,name='detail'),
]