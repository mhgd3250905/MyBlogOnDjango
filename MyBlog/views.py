from django.shortcuts import render
from MyBlog.BmobUtils import QueryUtils
from MyBlog.models import SKBlog
from django.core import serializers
import json
import time

# Create your views here.

def blog(request):
    '''
    首页，不解释
    :param request:
    :return:
    '''
    return  render(request,"blogNew.html",{'host':'http://127.0.0.1:8000/'})

def spider(request,tableName=None):
    '''
    显示所有的爬虫资讯页面
    :param request: tableName
    :param tableName:
    :return:
    '''
    #从爬虫工具模块中查询list类型的返回结果
    beanList = []
    if tableName == None:
        tableName = "HXBean"
    beanList = QueryUtils.queryBmob(tableName, index=0)
    #将查询到的list数据传递到模板中
    return render(request,"spiderNew.html",{'title':'盛大开的爬虫资讯','posts':beanList,'host':'http://127.0.0.1:8000/'})

def edit(request):
    '''
    编辑界面
    :param request:
    :return:
    '''
    #跳转到编辑界面
    return render(request,"editNew.html")

def recieve_data(request):
    '''
    编辑界面中提交按钮的作用
    通过POST异步操作把编写的文档传递到后台数据库
    :param request:
    :return:
    '''
    #判断请求类型：如果是POST
    if request.method == 'POST':
        #获取传递数据中的title内容
        title=request.POST['title']
        #获取传递数据中的content内容
        content=request.POST['content']
        #获取..
        shortContent = request.POST['shortContent']
        #生成提交时候的时间戳按毫秒记录：后面作为ID来查询各种
        revisedTime='%d' % time.time()
        #在数据库中创建对应的模板数据
        SKBlog.objects.create(title=title,revisedTime=revisedTime,content=content,shortContent=shortContent)
        return render(request,'Base.html')
    else:
        return render(request,'Base.html')

def showBlog(request):
    '''
    博客列表
    :param request:
    :return: 博客列表
    '''
    #获取所有的博客
    skblogs=SKBlog.objects.all()
    #序列化处理所有到的博客
    data= serializers.serialize("json", skblogs)
    #把序列化后的博客们转化为字典模式
    blogs=eval(data)
    # print(type(blogs))
    # print(blogs)
    #包含所有博客的字典传递到模板中
    return render(request,'blogNew.html',{'title':'盛大开的博客','blogs':blogs})

def blogDetails(request,blogId):
    '''
    通过blog对无二的时间id来查询对应的博客内容
    然后跳转到对应的博客详情
    :param request: blogId
    :param blogId:
    :return: 博客详情
    '''
    # 获取指定博客
    blog=SKBlog.objects.get(revisedTime=blogId)
    # 获取博客title
    title=blog.title
    # 获取博客content
    content=blog.content
    #获取博客时间
    revisedTime=blog.revisedTime
    #json序列化需要在JS中使用的content
    jsonBlog=json.dumps({'content':content})
    # 传递到博客详情的页面中
    return render(request,'blogDetail.html',{'title':title,'revisedTime':revisedTime,'blog':jsonBlog})

