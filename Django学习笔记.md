2017/1/6 13:45:18 
----------
#开始学习Django


> 使用了PyCharm一键式搭建Django所以基本配置就不多说了


#第一个问题

###将博客从falsk移植到Django的时候静态文件配置出了问题###

解决方法

Django setting.py中设置如下：

	STATIC_URL = '/static/'

在模板中使用：

	{% load staticfiles %}
	<link rel="stylesheet" type="text/css" href={% static 'css/bootstrap.min.css' %}>
	<link rel="stylesheet" type="text/css" href={% static 'css/bootstrap-theme.min.css' %}>
	<link rel="stylesheet" type="text/css" href={% static 'css/styleBlog.css' %}>
便可以正常的显示渲染之后的网页了

----------
#问题：2

views 以及 url的配置

目前我需要展示的网页有两个：

> 主页
> 
> 爬虫页面
### 完成如下 ###

首先是Views：
	from django.shortcuts import render
	from MyBlog.BmobUtils import QueryUtils

	def blog(request):
    	return  render(request,"Base.html",{'host':'http://127.0.0.1:8000/'})

	def spider(request,spider,tableName=None):
    	beanList = []
    	if tableName == None:
        	tableName = "HXBean"
		beanList = 	QueryUtils.queryBmob(tableName, index=0)
    	return render(request,"spiderNew.html",{'title':'盛大开的爬虫资讯','posts':beanList,'host':'http://127.0.0.1:8000/'})

这里定义两个方法分别是返回**主页HTMl模板**以及**爬虫显示HTML模板**

**需注意的是**这里通过QueryUtils模块来获取爬虫的数据然后传递给模板时候参数传递与flask有一些不同：

	from django.shortcuts import render
	
	return render(request,"spiderNew.html",{'title':'盛大开的爬虫资讯','posts':beanList,'host':'http://127.0.0.1:8000/'})

> 三个参数：

> 1：request（必须）

> 2：模板位置

> 3：字典形式的数据传递（模板中引用的方法与falsk一致）
	




