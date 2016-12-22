# coding:utf-8
from django.shortcuts import render,get_object_or_404

from .models import Article
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.template import loader

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def index(request):
    # print 'index'
    article_list = Article.objects.order_by('-pub_date').filter(publish=True)
    # 分页
    paginator = Paginator(article_list,5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage :
        articles = paginator.page(paginator.num_pages)

    return render(request,'blog/index.html',{'articles':articles})
    # template = loader.get_template('blog/index.html')
    # return HttpResponse(template.render(articles,request))


# class IndexView(generic.ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'lastest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]

def articleByTag(request,tag):
    # print tag
    article_list_tag = Article.objects.order_by('-pub_date').filter(publish=True,article_tag=tag)
    # 分页
    paginator = Paginator(article_list_tag,5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage :
        articles = paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',{'articles':articles})
 
# 关于我页面
def about(request,tag):
    # print 'about'
    return render(request,'blog/about.html')

def star(request,article_id):
    article = get_object_or_404(Article,pk=article_id)
    article.star += 1
    article.save()
    return HttpResponseRedirect(reverse('blog:detail',args=(article_id,)))
    

def detail(request,article_id):
    article = get_object_or_404(Article,pk=article_id)

    return render(request,'blog/detail.html',{'article':article})
    