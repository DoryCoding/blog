# coding:utf-8
from django.shortcuts import render,get_object_or_404

from .models import Article
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.template import loader

# Create your views here.
def index(request):
    article_list = Article.objects.order_by('-pub_date')
    # print article_list
    articles = {
        'article_list':article_list,
    }
    # print articles
    return render(request,'blog/index.html',articles)
    # template = loader.get_template('blog/index.html')
    # return HttpResponse(template.render(articles,request))


# class IndexView(generic.ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'lastest_question_list'

#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]