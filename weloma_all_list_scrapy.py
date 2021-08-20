'''------------------------------------------------------------------------------------------------------

#本项目主要用于将漫画网站里的网页代码按顺序下载到本地的网页文件里
#漫画网站：https://weloma.net

------------------------------------------------------------------------------------------------------'''
import time
import os
import requests
from bs4 import BeautifulSoup

def GeiYePa(url, header,title):

    response = requests.get(url, headers=header)                                                 #发送带有请求头的请求
    print(response)                                                                              #输出响应信号
    page_content = response.content.decode("utf-8")                                              #将网页内容以utf-8的编码格式输出
    #print(page_content)                                                                          #保存
    #open(f"E:\\scrapy_result\\白毛jk\\result.html", "w", encoding="utf-8").write(page_content)   #保存网页

    #解析环节
    soup = BeautifulSoup(page_content, "html.parser")
    imgs = soup.find_all(name='img')                                                              #获取网页里关于所有img标签的数组
    #print(imgs)
    num = 1
    for a in imgs:                                                                                #遍历img标签数组里的所有值
        data_address = a.get('data-aload')                                                        #用get方法将每个img标签里面对应的属性抽取出来
        if data_address !=  None:                                                                 #只对有src值的img标签进行操作
            data_address=data_address.split()[0];                                                 #返回的src值里有一行空行，此处将其处理了
            #print(data_address)
            response = requests.get(data_address, headers=header)  # 发送带有请求头的请求
            print(response)
            #time.sleep(5)                                                                        #延时装置
            print(f"{num}.jpg downloading")
            mypath=f'E:\\scrapy_result\\kobayashi\\{title}'
            if os.path.exists(mypath):                                                            #判断该文件夹是否存在
                open(f"{mypath}\\{num}.jpg", "wb").write(response.content)                        #将response的内容(即图片)保存
            else:
                os.mkdir(mypath)                                                                  #如该文件夹不存在，则创建文件夹
                print("folder created")
                open(f"{mypath}\\{num}.jpg", "wb").write(response.content)                        #将response的内容(即图片)保存
            num += 1
    print('download is over')
    return 0
