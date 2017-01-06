# -*- coding: utf-8 -*-
import requests

#查询URL： https://api.bmob.cn/1/classes/TableName

headers={
    'X-Bmob-Application-Id':'9e16e39fa5374f446e5c928da0f83d62',
    'X-Bmob-REST-API-Key':'42db163cd4c45884279b914e1c2a4e75',
    'Content-Type':'application/json'
}
data={
    'limit':'200'
}


def queryBmob(tableName,index):
    '''
    查询制定table的数据然后返回一个List<Bean>
    :param tableName:
    :return: List<Bean>
    '''
    beanList=[]
    url='https://api.bmob.cn/1/classes/%s?limit=20&skip=%d&order=-createdAt' % (tableName,index*20)
    response=requests.get(url,headers=headers,data=data).json()
    # print(response)
    rosponseList=response['results']
    # for item in rosponseList:
    #     title=item['title']
    #     print(title)
    #     contentUrl=item['contentUrl']
    #     print(contentUrl)
    #     imgUrl=item['imgUrl']
    #     print(imgUrl)
    #     HXBean=Bean.DataBean(title,contentUrl,imgUrl)
    #     beanList.append(HXBean)

    return rosponseList


