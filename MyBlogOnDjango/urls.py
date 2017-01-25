"""MyBlogOnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from MyBlog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.showBlog),
    url(r'^spider/(?P<tableName>.*)/',views.spider),
    url(r'^edit/$',views.edit),
    url(r'^upload/$',views.recieve_data),
    url(r'^blog/$',views.showBlog),
    url(r'^blog/(?P<blogId>(\d)*)/$',views.blogDetails)
]
