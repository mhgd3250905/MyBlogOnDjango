#2017/1/7 21:31:42 
----------
#视图学习

##视图装饰器
###限制HTTP的请求方法

> 限制视图只能服务规定的http方法

	from django.views.decorators.http import require_http_methods
	@require_http_methods(["GET", "POST"])
	def my_view(request):
    	# I can assume now that only GET or POST requests make it this far
    	# ...
    	pass

注意：**HTTP请求的方法名必须大写**

> require_GET()： 只允许视图接收GET方法的装饰器
> 
> require_POST(): 只允许视图接收POST方法的装饰器
> 
> require_safe()： 只允许视图接收GET和HEAD方法的装饰器。这些方法通常被人为是安全的，因为方法不该有请求资源以外的目的：
> 
> **备注**
> 
> Django 会自动清除对HEAD 请求的响应中的内容而只保留头部，所以在你的视图中你处理HEAD 请求的方式可以完全与GET 请求一致。因为某些软件，例如链接检查器，依赖于HEAD 请求，所以你可能应该使用require_safe 而不是require_GET。

...


----------
##文件上传

###基本的文件上传

考虑一个简单的表单，它含有一个**FileField：**

	# In forms.py...
	from django import forms
	class UploadFileForm(forms.Form):
    	title = forms.CharField(max_length=50)
    	file = forms.FileField()

> 这里创建了一个class继承自forms.Form

> 处理这个表单的视图会在request中接收到上传文件的数据
> 接收到的FILES是一个字典它包含每一个FileField的键（或者ImageField，FielField的子类）。这样的话就可以用request.FILES['file']来存放表单中的这些数据了

注意：**request.FILES只有在请求方法为POST，并且发送请求的
<form>拥有enctype="multipart、form-data"属性时，才会包含数据。否则request.FILES为空**

###一个简单的demo
	from django.http import HttpResponseRedirect
	from django.shortcuts import render_to_response
	from .forms import UploadFileForm

	# Imaginary function to handle an uploaded file.
	from somewhere import handle_uploaded_file

	def upload_file(request):
		#判断如果请求方式是POST
    	if request.method == 'POST':
			#将请求中的FILES绑定到form
        	form = UploadFileForm(request.POST, request.FILES)
			#如果绑定的form是有效的
        	if form.is_valid():
				#处理上传的文件
            	handle_uploaded_file(request.FILES['file'])
				#返回结果
            	return HttpResponseRedirect('/success/url/')
    	else:
			#如果是GET请求，那么就给予form一个空的
        	form = UploadFileForm()
    	return render_to_response('upload.html', {'form': form})

对于接收到的FILES，一般可以如下处理：

	def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

##使用模型处理上传文件
如果你在Model上使用FileField保存文件，使用ModelForm可以让这个操作更加容易。调用form.save()的时候，文件对象会保存在相应的FileField的upload_to参数指定的地方。

	from django.http import HttpResponseRedirect
	from django.shortcuts import render
	from .forms import ModelFormWithFileField

	def upload_file(request):
    	if request.method == 'POST':
        	form = ModelFormWithFileField(request.POST, request.FILES)
        	if form.is_valid():
            	# file is saved
           		form.save()
            	return HttpResponseRedirect('/success/url/')
    	else:
        	form = ModelFormWithFileField()
    	return render(request, 'upload.html', {'form': form})


如果你手动构造一个对象，你可以简单地把文件对象从request.FILE赋值给模型：

	from django.http import HttpResponseRedirect
	from django.shortcuts import render
	from .forms import UploadFileForm
	from .models import ModelWithFileField

	def upload_file(request):
    	if request.method == 'POST':
       		form = UploadFileForm(request.POST, request.FILES)
        	if form.is_valid():
            	instance = ModelWithFileField(file_field=request.FILES['file'])
            	instance.save()
            	return HttpResponseRedirect('/success/url/')
    	else:
        	form = UploadFileForm()
    		return render(request, 'upload.html', {'form': form})
	
	
	
	
	
	





