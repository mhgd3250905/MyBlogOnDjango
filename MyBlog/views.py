from django.shortcuts import render
from MyBlog.BmobUtils import QueryUtils

# Create your views here.
def blog(request):
    return  render(request,"Base.html",{'host':'http://127.0.0.1:8000/'})

def spider(request,spider,tableName=None):
    beanList = []
    if tableName == None:
        tableName = "HXBean"
    beanList = QueryUtils.queryBmob(tableName, index=0)
    return render(request,"spiderNew.html",{'title':'盛大开的爬虫资讯','posts':beanList,'host':'http://127.0.0.1:8000/'})

def edit(request):
    return render(request,"editNew.html")

