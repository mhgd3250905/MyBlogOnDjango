from django.shortcuts import render
from MyBlog.BmobUtils import QueryUtils
from MyBlog.models import SKBlog
import json
import time

# Create your views here.
def blog(request):
    return  render(request,"Base.html",{'host':'http://127.0.0.1:8000/'})

def spider(request,tableName=None):
    beanList = []
    if tableName == None:
        tableName = "HXBean"
    beanList = QueryUtils.queryBmob(tableName, index=0)
    return render(request,"spiderNew.html",{'title':'盛大开的爬虫资讯','posts':beanList,'host':'http://127.0.0.1:8000/'})

def edit(request):
    return render(request,"editNew.html")

def recieve_data(request):
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        shortContent = request.POST['shortContent']
        revisedTime='%d' % time.time()
        SKBlog.objects.create(title=title,revisedTime=revisedTime,content=content,shortContent=shortContent)
        print(SKBlog.objects.get(title=title).shortContent)
        return render(request,'Base.html')
    else:
        return render(request,'Base.html')

def showBlog(request):
    blog=SKBlog.objects.get(title="<h1>ksheng</h1>")
    jsBlog=blog.toJSON()
    print(jsBlog)
    return render(request,'blogNew.html',{'title':'盛大开的博客','blog':json.dumps(jsBlog)})

# def saveBolg(request):
