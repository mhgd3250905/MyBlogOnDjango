#2017/1/15 15:57:13


----------
#Django学习笔记_数据模型在html模板中的使用

项目需求是这样，我们从数据库中读取了需要的数据，然后渲染到模板之中

	blogs=SKBlog.objects.all()

如果我们直接把数据昨晚参数传入到模板中是无法直接使用的

所以这里需要将获取到的数据进行序列化 

## 1 序列化为json类型 ##
	from django.core import serializers
	data = serializers.serialize("json", blogs)

这样就获得了对应的json类型数据：

	[{'model': 'MyBlog.skblog', 'pk': 1, 'fields': {'title': 'asdasd', 'content': 'asdsadsad<p></p>', 'shortContent': 'asdsadsad', 'revisedTime': '1484392439'}}, {'model':...}]

## 2 json转dict ##
但是我们的模型中能够接受的仅仅是dict以及list，所以我们选择转化为[{}]的形式

	blogs=SKBlog.objects.all()
    data = serializers.serialize("json", blogs)
    print(eval(data))

这里选择使用**eval()**方法，获取到的数据传递到模板中：

	blogs=SKBlog.objects.all()
	    data = serializers.serialize("json", blogs)
	    print(eval(data))
	    return render(request,'blogNew.html',{'title':'盛大开的博客','blogs':eval(data)})

## 3 在模板中使用 ##
	
	 {% for blog in blogs %}
		<div id="showBlog" class="row clearfix">
		    <div class="col-md-12 column">
					<h3>
		                {{ blog.fields.title }}
					</h3>
					<p>
		                {{ blog.fields.shortContent }}
					</p>
				</div>
		</div>
	</div>
    {% endfor %}

> OK 大功告成~

#2017/1/17 21:37:07 
----------
##实例讲解：

1.从数据库获取需要的数据：

	blog=SKBlog.objects.get(revisedTime=blogId)

2.分解需要的数据：
	
	title=blog.title
    content=blog.content
    revisedTime=blog.revisedTime

> title和revisedTime使用在html中，而content使用在JS中

3.json序列化JS中需要的数据

	jsonBlog=json.dumps({'content':content})

4.传递给模板

	return render(request,'blogDetail.html',{'title':title,'revisedTime':revisedTime,'blog':jsonBlog})

5.在模板中使用

	{% extends "Base.html" %}
	{% load staticfiles %}
	
	{#标题#}
	{% block title %}
	    {{ title }}
	{% endblock %}
	
	{#内容#}
	{% block content %}
		<div class="row clearfix">
			<div class="col-md-12 column" id="blogContent">
	            <h3 class="text-center">
					  {{ title }}
				</h3>
			</div>
		</div>
	{% endblock %}
	
	{#JS#}
	{% block JS %}
	    <script>
	        $(function () {
	            var blog={{ blog|safe }};
	            $("#blogContent").append(blog.content);
	        })
	    </script>
	{% endblock %}

> 可以注意到这里JS中对于blog的使用：
> 首先使用 var blog={{ blog|**safe** }}获取到blog，然后在进行下一步操作