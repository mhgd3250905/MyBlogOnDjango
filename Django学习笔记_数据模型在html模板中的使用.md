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