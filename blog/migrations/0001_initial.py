# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='published date')),
                ('content', models.TextField(max_length=100000)),
                ('article_tag', models.CharField(choices=[('iOS', 'iOS'), ('Python', 'Python'), ('Git-SVN', 'git or svn'), ('JS', 'javascript'), ('Essay', 'essay')], max_length=10)),
                ('star', models.IntegerField(default=0)),
            ],
        ),
    ]