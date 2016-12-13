# coding:utf-8
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone

# Create your models here.
ARTICLE_TAG = (
    ('iOS','iOS'),
    ('Python','Python'),
    ('Git-SVN','git or svn'),
    ('JS','javascript'),
    ('Essay','essay'),
    )

@python_2_unicode_compatible
class Article(models.Model):
    # 标题
    title = models.CharField(max_length=200)
    # 创建时间
    pub_date = models.DateTimeField('published date')
    # 文章内容
    content = models.TextField(max_length=100000)
    # 文章类型
    article_tag = models.CharField(max_length=10,choices=ARTICLE_TAG)
    # 文章点赞数
    star = models.IntegerField(default=0)

    def __str__(self):
        return u'%s %s' % (self.title,self.content)
