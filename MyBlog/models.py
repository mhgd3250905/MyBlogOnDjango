from django.db import models

# Create your models here.
class SKBlog(models.Model):

    title=models.CharField(max_length=100)
    revisedTime=models.TextField(null=True,blank=True)
    revisedId=models.TextField(null=True,blank=True)
    content=models.TextField()
    shortContent=models.TextField()

    def __unicode__(self):
        '''
        输出数据内容
        :return:
        '''
        return '标题：'+self.title