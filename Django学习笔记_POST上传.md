#2017/1/14 23:29:24 
----------
# Django学习笔记 POST上传数据 #

> 普通的GET请求就不多说了
> 这一次的需求是需要把一些数据通过POST回传到后端

## 1 请求URL&视图函数 ##
首先我们创建一个url接收器：
	
	from django.conf.urls import url
	from django.contrib import admin
	from MyBlog import views

	urlpatterns = [
	    url(r'^admin/', admin.site.urls),
	    url(r'^upload/$',views.recieve_data),
	]

这里**views.receive_data**函数就是对应处理post请求的视图函数

接下来我们创建一个处理POST请求的视图函数：

	def recieve_data(request):
	    if request.method == 'POST':
	        ...
	        return render(request,'Base.html')
	    else:
	        return render(request,'Base.html')

这里可以看到，在视图函数中我们对请求做了判断：是否为POST请求，使用的**request.method**属性

在判断了POST以后我们对我们具体的数据内容进行分析，先看一下我们的html内容：

![](http://i.imgur.com/GGK96uV.png)


很明确，当用户点击提交按钮之后，我们将日志的标题以及内容传送回后端
	
	$("#textSave").click(function(){
        //获取输入的标题以及内容
        var textTitle=$("#formGroupInputLarge").val()
        var textHtml=editor.$txt.html()
        var textShort=editor.$txt.text()
        //通过post方式回传
        $.post("/upload/",
        {
            title:textTitle,
            content:textHtml,
            shortContent:textShort
        };

这里使用了jQuery的异步请求方式
	
	$.post("/upload/",
        {
            title:textTitle,
            content:textHtml,
            shortContent:textShort
        }

> $.post()参数最多三个，分别为：url/data/回调函数
> 
> 这里没有回调函数，返回的数据为标题/内容/纯文本内容

那么我们如何在视图函数中获取这些请求的数据呢？

解决方法当然都在我们的必备参数**request**之中：

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

> 通过**request.POST[参数key]**来获取对应的数据内容

测试一下：

![](http://i.imgur.com/CkkPzdD.png)

输出了我们的内容，OK！

当然，这里使用了设置好的数据模型来保存数据