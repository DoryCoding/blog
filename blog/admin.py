# coding:utf-8
from django.contrib import admin
from django import forms

from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','article_tag','star','publish')
    # list_editable = ('publish',)
    ordering = ('-pub_date',)
    date_hierarchy = 'pub_date'
    list_per_page = 10
    radio_fields = {"article_tag": admin.VERTICAL}
    readonly_fields = ('star',)
    search_fields = ('title',)
    # list_filter = ('title','pub_date')
        

# admin.site.register(Article,ArticleAdmin)
admin.site.register(Article,ArticleAdmin)