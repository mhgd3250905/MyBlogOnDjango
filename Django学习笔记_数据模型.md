#2017/1/15 1:02:05 

----------
# Django学习笔记之数据模型 #

## 1 创建模型 ##

首先我们在项目中创建一个数据模型：

	from django.db import models
	
	# Create your models here.
	class SKBlog(models.Model):
	
	    title=models.CharField(max_length=100)
	    revisedTime=models.TextField()
	    content=models.TextField()
	    shortContent=models.TextField()
	
	    def __unicode__(self):
	        '''
	        输出数据内容
	        :return:
	        '''
        return '标题：'+self.title

创建的数据模型需要继承**models.Model**

## 2 同步数据库 ##

在创建好了数据模型之后，我们需要进行同步数据库操作：

	注意：Django 1.7 及以上的版本需要用以下命令
	python manage.py makemigrations
	python manage.py migrate

在同步好数据库中后我们就可以发现数据库中多了SKBlog table了

## 3 使用数据模型 ##

**以数据模型保存数据**：

### ⑴ 创建数据模型 ###

	SKBlog.objects.create(title=title,revisedTime=revisedTime,content=content,shortContent=shortContent)
或者
	
	skBlog=SKBlog（title=title,revisedTime=revisedTime,content=content,shortContent=shortContent）
	skBlog.save()

或者 
	
	skBlog=SKBlog()
	skBlog.title=title
	skBlog.revisedTime=revisedTime
	skBlog.content=content
	slBlog.shortContent=shortContent
	skBlog.save()
或者

	SKBlog.objeats.get_or_create（title=title,revisedTime=revisedTime,content=content,shortContent=shortContent）
	
**这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，第一个为SKBlog对象，第二个为True或False, 新建时返回的是True, 已经存在时返回False.**

### ⑵ 获取数据模型 ###

	#获取指定的一个
	blog=SKBlog.objects.get(title='aaa')
	#获取所有
	blogs=SKBlog.objects.all()
	#切片操作,获取前面十个
	blogs=SKBlog.objects.all()[:10]
	

