#2017/1/6 18:02:23 
----------
#正式开始花功夫学习Django，难道还能比Android更难？？？

##URL调度器##
示例：

	from django.conf.urls import url
	from . import views
	urlpatterns = [
    	url(r'^articles/2003/$', views.special_case_2003),
    	url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    	url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    	url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
	]

> 知识点：
> 通过URL传递有命名的参数给视图函数

	/articles/2005/03/ 
	请求将调用views.month_archive(request, year='2005', month='03')函数
	而不是views.month_archive(request, '2005', '03')。

##对于传入的的参数，其匹配/分组算法如下：

1.如果有命名参数，则使用这些命名参数，忽略非命名参数

2.否则，它将已位置参数传递所有的非命名参数。

> 另：捕获的参数都是字符串：

例如：

	url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive)

其中的year参数虽然由[0-9]{4}匹配整数，但year=‘匹配内容’



----------

##指定参数的默认值
	
有一个方便的小技巧是指定视图参数的默认值。 下面是一个URLconf 和视图的示例：

	# URLconf
	from django.conf.urls import url
	from . import views
	urlpatterns = [
    	url(r'^blog/$', views.page),
    	url(r'^blog/page(?P<num>[0-9]+)/$', views.page),
	]

	# View (in blog/views.py)
	def page(request, num="1"):
    # Output the appropriate page of blog entries, according to num.
    ...


----------
##包含其它的URLconfs

这里理解为一种方便的写法，先看一个例子：

	from django.conf.urls import include, url
	from apps.main import views as main_views
	from credit import views as credit_views

	extra_patterns = [
    	url(r'^reports/(?P<id>[0-9]+)/$', credit_views.report),
    	url(r'^charge/$', credit_views.charge),
	]

	urlpatterns = [
    	url(r'^$', main_views.homepage),
    	url(r'^help/', include('apps.help.urls')),
	url(r'^credit/', include(extra_patterns)),
	]

> 然后键入一个URL如下：
> /credit/reports/1992/
> 这个URL将会被credit.views.report() 这个Django 视图处理。

###所以对于如下的冗长的代码我们可以进行精简
	
	from django.conf.urls import url
	from . import views
	urlpatterns = [
    	url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/history/$', views.history),
    	url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/edit/$', views.edit),
    	url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/discuss/$', views.discuss),
    	url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/permissions/$', views.permissions),
	]

###我们可以改进它，通过只声明共同的路径前缀一次并将后面的部分分组：

	from django.conf.urls import include, url
	from . import views

	urlpatterns = [
    	url(r'^(?P<page_slug>[\w-]+)-(?P<page_id>\w+)/', include([
        	url(r'^history/$', views.history),
        	url(r'^edit/$', views.edit),
        	url(r'^discuss/$', views.discuss),
        	url(r'^permissions/$', views.permissions),
    	])),
	]

##捕获的参数

被包含的URLconf 会收到来自父URLconf 捕获的任何参数，所以下面的例子是合法的：

	# In settings/urls/main.py
	from django.conf.urls import include, url

	urlpatterns = [
    	url(r'^(?P<username>\w+)/blog/', include('foo.urls.blog')),
	]

	# In foo/urls/blog.py
	from django.conf.urls import url
	from . import views

	urlpatterns = [
    	url(r'^$', views.blog.index),
    	url(r'^archive/$', views.blog.archive),
	]

在上面的例子中，捕获的"username"变量将被如期传递给include()指向的URLconf。

----------
##传递额外的选项给视图函数

django.conf.urls.url() 函数可以接收一个可选的**第三个参数**，它是一个字典，表示想要传递给视图函数的额外关键字参数。

例如：

	from django.conf.urls import url
	from . import views

	urlpatterns = [
    	url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive, {'foo': 'bar'}),
	]

> 上面的例子中对于 /blog/2005/请求
> Django 将调用views.year_archive(request, year='2005', foo='bar')

###处理冲突

URL 模式捕获的命名关键字参数和在字典中传递的额外参数有可能具有相同的名称。当这种情况发生时，将使用**字典中的参数**而不是URL 中捕获的参数。


> 当然，第三个参数也会传递到include包含的url中