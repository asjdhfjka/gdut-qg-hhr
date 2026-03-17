#1.网络请求
# https://www.baidu.com  --url 统一资源定位符
#请求过程:
#客户端，指web浏览器向服务器发送请求
#请求-分为四部分:
#1.请求网址--request url
#2.请求方法--request methods
#3.请求头--request header
#4.请求体 -- request body
#F12查看请求响应
# import requests#导入库
# url = 'https://www.bilibili.com/'#找到目标url
# response = requests.get(url)#发送请求
# print(response.text)#打印响应，响应内容有乱码，requests模块会自动寻求一种解码方式去解码
# #打印不出来是因为被屏蔽了
# print(response.content.decode())#解码的另外一种方式,默认utf-8解码
# import requests
#
# url = 'https://img0.baidu.com/it/u=2157475748,780862469&fm=253&app=138&f=JPEG?w=800&h=1237'
# res = requests.get(url)
# print(res.content)
# with open('1.jpg', 'wb') as f:
#     f.write(res.content)#图片类型是wb，文字是w
#其他属性
#response.text和response.content的区别:
#text: str类型，requests模块自动根据http头部对响应的编码作出有根据的推测
#content:bytes类型，可以通过decode()解码，一般用于图片视频等
# import requests
# url = 'https://www.baidu.com/'
# #headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
# response = requests.get(url)
# print(1)
# print(response.content.decode())
# print(response.text)
# import requests
# url = 'https://www.baidu.com/index.php?tn=68018901_58_oem_dg'
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'}
# response = requests.get(url, headers=headers)
# print(len(response.content.decode()))
# print(response.request.headers)#可以打印出请求头
# user-agent池--防止防爬
#随机调用
#第一种构建池
# import random
# UAlist = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/139.0.0.0',
#     'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36 Edg/139.0.0.0'
# ]
# print(random.choice(UAlist))
#第二种用库fake_useragent，可能会出现异常
# from fake_useragent import UserAgent
# print(UserAgent().random)
# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com")
# html = response.read()
# # print(html)
# import urllib.request
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.read()
# print(html)
# import requests
# for a in range(0,50):
#     try:
#         response = requests.get('http://www.baidu.com',timeout=0.01)
#         print(response.status_code)
#     except Exception as e:
#         print('异常'+str(e))
# from urllib.request import urlopen
# url = 'http://www.baidu.com'
# response = urlopen(url)
# html = response.read()
# # print(html.decode('utf-8'))
# with open('mybaidu.html',mode='w',encoding='utf-8') as f:
#     f.write(html.decode('utf-8'))
'''get请求'''
import re
import time
from time import sleep

# import requests
# content = input('请输入你想要的信息：')
# url = f'https://cn.bing.com/search?q={content}form=ANNTH1&refig=68a6c27b6f364ab68c4121f91b77df4b&pc=ASTS'
# headers = {
#     'user-agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
# }
# resp = requests.get(url,headers=headers)
# print(resp.text)
'''post请求'''
# import requests
# url = 'https://fanyi.baidu.com/sug'
# hehe = {'kw':input('请输入字母：')}#这里要字典形式
# headers = {
#     'user-agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
# }
# resp = requests.post(url,data=hehe,headers=headers)
# print(resp.text)#拿到的是文本字符串
# print(resp.json()['data'])#拿到的是json数据，出来是字典，方便抽取你要的数据
# '''两者的差距在要请求的参数的位置不一样一个在问号后面，一个在data后面'''
# import requests
# url = 'https://movie.douban.com/j/chart/top_list'
# data = {
# 'type':'13',
# 'interval_id':'100:90',
# 'action':'',
# 'start':'0',
# 'limit':'20',
# }
# headers = {
# 'user-agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
# }
# resp = requests.get(url,params=data,headers=headers)
# print(resp.text)
# print(resp.request.url)
# #get请求永远在url身上
# print(resp.json())
# import re
#
# result = re.findall(r'\d+','我是你爸爸，wyx是sb，他有10块钱,666666')
# print(result)
#
# result_1 = re.finditer(r'\d+','我是你爸爸，wyx是sb，他有10块钱,666666')
# for i in result_1:#从迭代器中拿到内容
#     print(i.group())#从匹配到的结果中拿到数据
#
# result_2 = re.search(r'\d','我是你爸爸，wyx是sb，他有10块钱,666666')
# print(result_2.group())#search只会拿到第一次出现的你需要的数据
#
# result_3 = re.match(r'\d','我是你爸爸，wyx是sb，他有10块钱,666666')
# print(result_3)#默认\d前面有一^，即^\d，然后和search一样只取第一个找到的数据
#
# obj = re.compile(r'\d+')#预加载，提前把正则对象加载完毕
# result_4 = obj.findall('我是你爸爸，wyx是sb，他有10块钱,666666')#直接把加载好的正则进行运用
# print(result_4)
# import re
# wyx = '''<div class='西游记'><span id='10010'>中国联通</span></div
#        <div class='西游记'><span id='10086'>中国移动</span></div>'''
# obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")#多个引号的时候记得换引号不然电脑容易搞混乱
# result = obj.finditer(wyx)
# for i in result:
#     id = i.group("id")
#     name = i.group("name")#记得这一步
#     print(id)
#     print(name)
# #想要提取数据的时候必须要用小括号括起来，可以单独起名字
# #(?P<名字>正则)
# #提取数据的时候，需要group("名字")
# import requests
# import re
# f = open('top250.csv',mode='w',encoding='utf-8')#csv是每个元素之间用逗号相连接
# url = 'https://movie.douban.com/chart'
# headers = {
# 'user-agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0'
# }
# resp = requests.get(url,headers=headers)
# resp.encoding='utf-8'
# wyx = resp.text
# # print(resp.text)
# obj = re.compile(r'<tr class="item">.*?title="(?P<name>.*?)"'
#                  r'<div class="star clearfix">.*?<span class="rating_nums">(?P<score>.*?)</span>',re.S)#re.S使得.具有代替所有的能力，可以代替换行符
# result = obj.finditer(wyx)
# for item in result:
#     name = item.group('name')
#     score = item.group('score')
#     f.write(f'{name},{score}\n')
# f.close()
# resp.close()
# #.strip()去掉字符串左右两端的空白

# import re
# import requests
# url = 'https://www.dytt8899.com/'
# res = requests.get(url)
# res.encoding='gbk'
# obj = re.compile(r'2025必看热片.*?<ul>(?P<html>.*?)</ul>',re.S)
# result = obj.search(res.text)
# html = result.group('html')
# # print(html)
# obj_1 = re.compile("<li><a href='(?P<href>.*?)' title")
# result_1 = obj_1.finditer(html)
# obj_2 = re.compile(r'<div id="Zoom">.*?◎片　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)</tr>',re.S)
# for i in result_1:
#     # print(i.group('href'))
#     child_url = url.strip('/') + i.group('href')
#     child_res = requests.get(child_url)
#     child_res.encoding ='gbk'
#     result_2 = obj_2.search(child_res.text)
#     # print(result_2.group('name'))
#     # print(result_2.group('download'))
#     name = result_2.group('name')
#     download = result_2.group('download')
#     print(name,download)

# from bs4 import BeautifulSoup
# html ='''
# <ul>
#      <li><a href="zhangwuji.com">张无忌</a></li>
#      <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
#      <li><a href="zhubajie.com">猪八戒</a></li>
#      <li><a href="wuzetian.com">武则天</a></li>
# </ul>
# '''
# page = BeautifulSoup(html, 'html.parser')
# li = page.find('li',attrs={'id':'abc'})#标签名，属性，值后面两个是字典形式
# li_1 = page.find_all('li')#找到所有满足条件的
# li_2 = page.find('li')#只会找到一个满足条件的第一个
# # print(li_1)
# # print(li)
# # print(li_2)
# # a = li.find('a')
# # print(a)
# # print(a.text)#拿文本
# # print(a.get('href'))#拿属性，get('属性名')
# for i in li_1:
#     a_1 = i.find('a')
#     text = a_1.text
#     href = a_1.get('href')
#     print(text,href)

# import requests
# from bs4 import BeautifulSoup
# import re
# n = 2
# url = requests.get('http://tshare.cc/pbbz')
# url_1 = 'http://tshare.cc/'
# # print(url.text)
# page = BeautifulSoup(url.text, 'html.parser')
# a_list = page.find_all('a',attrs={'class':"media-img lazy bg-cover bg-center"})
# # print(a_list)
# for i in a_list:
#     href = i.get('href')
#     response = requests.get(href)
#     # print(response.text)
#     # break
#     bs = BeautifulSoup(response.text, 'html.parser')
#     article = bs.find('article',attrs={'class':"post-content"})
#     image_src = article.find('img').get('src')
#     # print(image_src)
#     image_res = requests.get(image_src)
#     with open(f'{n}.jpg', 'wb') as f:
#         f.write(image_res.content)
#     print(f'{n}图片已经下载完毕')
#     n+=1
# #子页面的url如果开头是/,直接在前面拼接上域名即可子页面的url不是/开头，此时需要找到主页面的url，去掉最后一个/后面的所有内容，和当前获取到的url进行拼接
# from lxml import etree
# xml = '''
# <book>
#     <id>1</id>
#     <name>野花遍地香</name>
#     <price>1.23</price>
#     <nick>臭豆腐</nick>
#     <author>
#         <nick id="10086">周大强</nick>
#         <nick id="10010">周芷若</nick>
#         <nick class="jay">周杰伦</nick>
#         <nick class="jolin">蔡依林</nick>
#         <div>
#             <nick>惹了</nick>
#         </div>
#     </author>
#     <partner>
#         <nick id="ppc">胖胖陈</nick>
#         <nick id="ppbc">胖胖不陈</nick>
#     </partner>
# </book>
# '''
# et = etree.XML(xml)
# # result = et.xpath('/book')      #/ 表示根节点
# # result = et.xpath('/book/nick/text()')[0]       #[0]表示去除列表只要文字
# # result = et.xpath('/book/name/text()')
# # result = et.xpath('/book//nick/text()')         #// 表示子子孙孙全部后代
# # result = et.xpath("/book/*/nick/text()")    #* 表示通配符表示所有人
# # result = et.xpath('/book/author/nick[@class="jay"]/text()')     #[]表示属性筛选，@属性名=值
# # result = et.xpath('/book/partner/nick/@id')       #最后那里表示拿到nick里面id的内容不用打text，直接@属性即可
# # result = et.xpath('/book/author/nick[2]/text()')    #nick后面的[2]是锁定了第二个
# print(result)

# from lxml import etree
# html ='''
# <ul>
#      <li><a href="zhangwuji.com">张无忌</a></li>
#      <li id="abc"><a href="zhouxingchi.com">周星驰</a></li>
#      <li><a href="zhubajie.com">猪八戒</a></li>
#      <li><a href="wuzetian.com">武则天</a></li>
# </ul>
# '''
# et = etree.HTML(html)
# li_list = et.xpath('//li')
# # print(li_list)
# for i in li_list:
#     href = i.xpath('./a/@href')[0]    #./表示当前节点
#     name = i.xpath('./a/text()')[0]
#     print(name, href)


# import requests
# from lxml import etree
# url = 'https://www.zbj.com/fw/?k=saas'
# headers = {'user-agent':
# "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0"}
# resp = requests.get(url,headers=headers)
# # print(resp.text)
# et = etree.HTML(resp.text)
# divs = et.xpath('//div[@class="search-result-list-service"]')
# for div in divs:
#     price = div.xpath('./div/div/div[3]/div[1]/text()')[0]
# print(price)

# import requests
# url = 'https://user.17k.com/ck/user/mine/readList?page=1&appKey=2406394919'
# resp = requests.get(url,headers={'Cookie':'GUID=3d5d70ab-c7a1-4499-bf14-804b32bb0e2b; acw_sc__v2=68b27b01cb7c36d4d490b4929b8e022736a39f4c; sajssdk_2015_cross_new_user=1; Hm_lvt_9793f42b498361373512340937deb2a0=1756527357; HMACCOUNT=CCED91CAD58606C3; tfstk=gHjtL49ogWViJ4hZBs4nnP90OWw3qyXNs1WSmIAil6Cd3snijnxMlKOpHftGh55ADB1Bs1bGn6HNv_nmj5zNhmKDc7VuquXNIn-bZxtvTYhwHKM_mCisdhJ02SDSWuXNQvGUZYhTqxL5CZA6GsT6Rp9DOjtXlFwpOKprlf1XcJepHKosCKtjdB9JnnOfGnwddBJXcd1XcJBBTKGvU-AIuIiAW8t_ePzwHmifvdLQ-OOCT6eDCFENIBibNMptcQ669miXwl5DG9Bg60WHbMfJE1qIX_B1Ps_5Okn98N6dDUSqUDWdFwbkWwFsDBjMHUtXJxifphOXPGt7VXpFRObfb1HxcdSGqEdyJ-i2oHskPa1t38WBfK12ziVrbC6fUg7k2onBXEsPCgjJwjckwK0TpJ3quF9EctW2k2LbdIJpZRUmuq83PpdupJ3quF9epQ2h2qu2-z1..; accessToken=nickname%3D%25E4%25B9%25A6%25E5%258F%258B9A9I8fpJw%26avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F65%252F93%252F104259365.jpg-88x88%253Fv%253D1756527435000%26id%3D104259365%26e%3D1772079460%26s%3D2934de9b1a685b51; c_channel=0; c_csc=web; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104259365%22%2C%22%24device_id%22%3A%22198f9306d171395-0c3e3f9dfb7ce6-4c657b58-1821369-198f9306d181b3b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%223d5d70ab-c7a1-4499-bf14-804b32bb0e2b%22%7D; ssxmod_itna=eqAx0DgDcDBQq0KP0dGQDHQySCDUrrf4mD7KqAxdfxD/KADnqD=GFDK40EE84KqdKfA0G4P6YFfw5qzzhROeeY8hGGdq6Db74GLDmKDy32oReDxpq0rD74irDDxD3vxneD+D04CMyhqi3D4qDRDAQDzdQBlBvSGT=DmdiDGkIXD7QDIktqDDNqDcGxiDWDbxUM/4R4XeDS3gU5GqDMReGXW0FqGkRkucGZUq9536PctliDtqD93etDb3jdX7U/3c448E4UDf4KIBAx3ODKjRGbGGLxf7fNQRqYIGGhebxbvXwoDbPqDDf6cH5eD=; ssxmod_itna2=eqAx0DgDcDBQq0KP0dGQDHQySCDUrrf4mD7KqAxdPG97ddoDBwxRq7P+xpkBOGFKCu061imPlFRxY3hjR0kQllWEiPDoAWkoPYdAjbEztq+iojzqibGhRIZQGjenszGeVd/s3Yz4EkVW4zpj9Nc2WNalpbUPTalE9CFgvC5fetVZuOxgAhl7HzHKfIc2qQRiWmAf3HWE3WI04Dwo5DLxG7KYD===; Hm_lpvt_9793f42b498361373512340937deb2a0=1756527666'}
#              )
# print(resp.json())


# import requests
# url = 'https://www.pearvideo.com/video_1801967'
# contID = url.split('_')[1]
# videostatus = f"https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.693225427699769"
# headers = {
#     'user-agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
# 'referer':
# 'https://www.pearvideo.com/video_1801967'      #反盗链，就是溯源，当前请求的上一级是谁
# }
# resp = requests.get(videostatus, headers=headers)
# # print(resp.text)
# dic =resp.json()
# Srcurl = dic['videoInfo']['videos']['srcUrl']
# systemTime = dic['systemTime']
# Srcurl = Srcurl.replace(systemTime,f'cont-{contID}')
# # print(Srcurl)
# with open('a.mp4','wb')as f:
#     f.write(requests.get(Srcurl).content)
# print('已经下载好了')


# import requests
# url = 'https://www.pearvideo.com/video_1802112'
# contID = url.split('_')[1]
# resp = requests.get(url)
# resp.encoding='utf-8'
# url_0 = f'https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.9128985513940328'
# headers = {
# 'user-agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
# 'referer':
# 'https://www.pearvideo.com/video_1802112',
# 'cookie':
# 'PEAR_UUID=b089f740-0d65-4969-9952-761923c9998b; _uab_collina=175653785593837573098847; p_h5_u=A98A7878-29B8-4420-A9DF-EC129A42AD14; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1756537856,1756611947; HMACCOUNT=CCED91CAD58606C3; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1756613586; tgw_l7_route=92611af627df0b9b1cd8a442f9668c80; JSESSIONID=9451CDCF8AED9F553EBB26275123DAE9'}
# resp_0 = requests.get(url_0, headers=headers)
# resp_0.encoding = 'utf-8'
# # print(resp_0.text)
# dic = resp_0.json()
# # print(dic)
# srcUrl = dic['videoInfo']['videos']['srcUrl']
# systemTime = dic['systemTime']
# srcUrl = srcUrl.replace(systemTime,f'cont-{contID}')
# # print(srcUrl)
# with open('b.mp4','wb')as f:
#     f.write(requests.get(srcUrl).content)
# print('下载完毕')
#
# # print(resp.text)
# # https://video.pearvideo.com/mp4/short/20250828/cont-1802090-16060217-hd.mp4
# # https://video.pearvideo.com/mp4/short/20250828/1756612389141-16060217-hd.mp4


# from threading import Thread
# class MyThread(Thread):
#     def run(self):   #固定的，当线程被执行时，被执行的就是run
#         for i in range(1000):
#             print('子线程' , i)
# if __name__ == '__main__':
#     t = MyThread()
#     t.start()   #开启线程
#     for i in range(1000):
#         print('主线程' , i)



# from multiprocessing import Pool   #这个是构建多进程稍微照着样子改一下就行了
# from threading import Thread    #这个是创建多线程
# def func(name):
#     for i in range(1000):
#         print(name,i)
#
# if __name__ == '__main__':
#     t1 = Thread(target=func,args=('王宇曦',))
#     t1.start()
#
#     t2 = Thread(target=func,args=('何华儒',))
#     t2.start()



# from concurrent.futures import ThreadPoolExecutor   #ThreadPoolExecutor这个是线程池，ProcessPoolExecutor这个是进程池
# def fn(name):
#     for i in range(100):
#         print(name,i)
# if __name__ == '__main__':
#     with ThreadPoolExecutor(50) as t:
#         for i in range(100):
#             t.submit(fn, name=f'线程{i}')
#     #with里面的执行完了才会执行外面的叫做守护
#     print('123')



# import asyncio
# async def func():
#     print('我是wyx')
#
# if __name__ == '__main__':
#     g = func()   #此时函数是一个异步协程函数，此时函数得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)


# import asyncio
# async def func1():
#     print('我是wyx')
#     time.sleep(3)
#     print('我是wyx')
#
#
# async def func2():
#     print('我是hhr')
#     time.sleep(2)
#     print('我是hhr')
#
#
# async def func3():
#     print('我是yjh')
#     time.sleep(4)
#     print('我是yjh')
#
# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [
#         f1,f2,f3
#     ]
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)






