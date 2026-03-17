# # print('Hello world','nihao',sep=',,,,,')
# # print('bingbing')
# # name_wyx=855
# name_hhr="nb"
# print(name_hhr)
# # name_wyx=250
# # print(name_wyx)
# # wyx=5
# # print(type(wyx))
# # wyx=2.50
# # print(type(wyx))
# print(True+5)
# print(False+2.5)
# # print(True+False)
# # ma=5+6j
# # mb=2+9j
# # print(type(ma))
# # print(ma+mb)
# wyx_1="""
# asdfh
# dsaf
# sdafads
# gasdg
# 你好325436"""
# wyx_2='sbbb'
# print(type(wyx_2))
# print(wyx_1)
# wyxmz="wyxez"
# wyxnl=18
# wyx_3="hhr"
# print('我的名字：%s，我的年龄：%d,我的父亲:%s'%(wyxmz,wyxnl,wyx_3))
# print('我是：%s,我的年龄是：%d,我的爸爸是：%s'%(wyxmz,wyxnl,wyx_3))
# a=250
# b=354
# print("%6d"%b)
# print('%06d'%b)
# print("%6d"%a)
# print('%06d'%a)
# b=1.2645568
# print('%f'%b)
# """遵循四舍五入，默认六位"""
# print('%.3f'%b)
# print('我是%%的%%'%())
# print(f'我叫{wyxmz},我今年{wyxnl}岁了')
# a=8
# b=9
# c=3
# d=5
# print(c/d)
# print(c//b)
# print(c%a)
# print(a/b)#商一定是浮点数
# print(a//b)#无四舍五入，只往下，取整数
# print(a%b)#取余数
# print(a**b)#幂运算
# a=99
# b=55
# a+=b#等效于a=a+b
# print(a)
# a=a+b+5
# print(a)
# """纯数字不能用赋值运算符，该运算针对变量存在"""
# hhr=input('我的名字是：')
# print("年龄\t性别\t电话")#默认四个空格
# print("哈哈哈哈\n嘻嘻嘻嘻")#换行
# print('wyx\rhhr')#将后面的东西放到前面本行的开头
# print('six\\star')
# print('six\\\\star')
# print(r'six\\\star')#r默认里面的所有内容取消转义
# cj=input('成绩=')
# cj=int(cj)
# if cj < 60:#有引号它为字符串
#     print('我是wangyuxi')
# a=999
# b=666
# print(a==b)#是否相等不用引号
# print(a!=b)#是否不同也不用引号
# if a>b:
#     print('a大于b')
# a='你好'
# b=6
# if a=='你好' and b==6:#注意两个等号，要两边同时成立
#     print('wyx是sb')
# a=3
# b=6
# if a==5 or b==6:#注意两个等号，其中一边成立就行
#     print('wyx是sb')
# hhr=666
# wyx=66
# print(not hhr>wyx)
# a=5
# b=8
# if a>b:
#     print('a大于b')
# else:
#     print('a小于b')
# print('a小于b') if a<=b else print('a大于b')
# a=45
# if 0 <=a<= 60:
#     print('不及格')
# elif 60<a<=85:
#     print('良好')
# elif 85<a<=100:
#     print('优秀')
# else:
#     print('分数无效')
# ticket=True
# temp=36
# if ticket==True:
#     print('可以进站了')
#     if 36.5<=temp<=38.5:
#         print('可以上车了')
#     else:
#         print('体温不正常不能上车')
# else:
#     print('不能进站')
# i=1
# while i<=5:
#     print('你真棒')
#     i+=1
# while True:
#     print('hlssb')
# """while Ture是死循环"""
# i=1
# s=0
# while i <= 100:
#     i += 1
#     s=s+i#两个顺序换了的话，这个代表的是1到101
# print('计算和等于:',s)#在循环内的话就会每个都进行计算
# i=1
# s=0
# while i <= 100:
#     s = s+i
#     i = i+1#这个代表的是1到100因为先进行前面的
# print('计算和等于：',s)
# i=1
# while i<=3:
#     print(f'这是第{i}次循环')
#     i=i+1
#     j=1
#     while j<=5:
#         print(f"这是第{j}次内循环")
#         j=j+1
# '''先外一次后内完全搞完后再进行外部第二次再接着内部继续一直循环直到结束'''
# str='helloworld'#定义一个字符串目前只有字符串可这么用
# for a in str:#可迭代对象就是要去一个一个取值的整体，现在只用知道字符串可以就行，a是临时变量可以随便写，i是常规写法
#     print(a)
# nb='1234'#正常写数字不行加上引号就变成了字符串就可以用了
# for b in nb:
#     print(b)
# for i in range(1,6):
#     print("我是你爹")
# for i in range(1,6):
#     print(i)#前闭后开
# for i in range(6):
#     print(i)#从0开始第一次
# s=0
# for i in range(1,101):
#     s+=i
# print(s)#相比之下for循环比while循环要简便一点
# i=1
# while i<=5:
#     print(f'wyx在吃第{i}沱屎')
#     if(i==3):
#         print("wyx吃饱了")
#         break
#     i+=1#这里的代码一步一步向下执行所以把它放在这里
# i=1
# while i<=5:
#     print(f'wyx吃到第{i}坨屎了')
#     if i==3:
#         print(f'wyx吃到第{i}坨屎的时候，吃到虫子了')
#         i = i+1#continue前一定要加上计数器否则可能进入死循环
#         continue
#     i=i+1
# for i in range(10):
#     if i==5:
#         break#当i=5时直接结束当前循环
#     print(i)
# for i in range(10):
#     if i==5:
#         continue#直接跳过i=5这个循环然后继续往下走
#     print(i)
# """两个都只对最近的一个循环起作用，对嵌套式不起作用"""
# a='hello'
# print(a,type(a))#str字符串以字符为单位进行处理
# a1=a.encode()#编码
# print(a1,type(a1))#bytes，以字节为单位进行处理
# a2=a1.decode()
# print(a2,type(a2))
# '''对于bytes只需要知道它可以和字符串之间进行转换'''
# st="我是王宇曦爸爸"
# st1=st.encode("utf-8")
# print(st1,type(st1))
# st2=st1.decode('utf-8')
# print(st2,type(st2))
# print(10+10)#对于数字时是计算符号
# print('10'+'10')#对于字符串时是合并的意思
# print(10*10)
# print('王宇曦是sb\n'*10)#在字符串中表示重复多少次
# name='wyx'
# print('b' in name)#是否存在
# print('w' in name)
# print('b'not in name)#是否不存在
# print('w'not in name)
# name='wyx是sb'
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])#找第几个位置的字符，下标从0开始的，从左往右的
# print(name[-2])#负数从右往左数,负数时-1代表了第一位
# st='asdfghjkl'
# """从左往右切割"""
# # print(st[1:5])#前闭后开，不包括第六位，从0开始的
# # print(st[:5])#第六位之前的都有不包括第六位
# # print(st[5:])#第六位之后的都有不包括第六位
# """切割的基本格式print(st[起始位置:终止位置:步长不写的话默认为1])"""
# print(st[-1::-1])#如此情况步长为-1，代表从右往左取值
# print(st[-1::1])#步长为1代表从左往右取值
# print(st[-1::-3])
# st='wyxshhrez'
# print(st[-1:-5:3])#这里前面两个意思是从右往左切割，后面表示从左往右切割，有误所以无法成功切割
# print(st[-1:-5:-3])#反之这个可以成功切割
# name='wysssb'
# print(name.find('y',2,5))#第一个位置是要找的元素，第二个位置是开始找的位置，第三个位置是结束寻找的位置
# '''若没找到则返回=1'''
# print(name.find('wys'))#找一个单元的时候，找到标识出来的数字是该单元第一个字符所在的位置
# '''同样的前闭后开'''
# print(name.index('wys'))#找不到就报错河find不太一样
# name='wyxssb'
# print(name.count('s',2,5))#同样遵循前闭后开的原则，代表你想要的东西重复出现了几次
# name='wyxssb'
# print(name.startswith('wyx',2,6))#在该区域内是否以你想要的东西开头是的话返回Ture不是的话返回False
# print(name.endswith('wyx',2,6))#检测在该区域内是否一你想要的东西结尾
# st='nihao'
# print(st.isupper())
# print('NIHAO'.isupper())#该符号表示你所指定的字符串是否全为大写是的话Ture不是的话为False
# name='何华儒是王宇曦爸爸'
# print(name.replace('爸','爹'))#
# print(name.replace('爸','爹',1))#修改内容后面不填数字的话就默认全部改变
# name='hello,world'
# print(name.split('o'))#分割符号，以指定的目标分割，返回的时候以列表的形式进行返回
# print(name.split('o',1))#指定只分割一次
# name='hello,WORld'
# print(name.capitalize())#第一个变成大写其他的全部变成小写
# print(name.lower())#全部变成小写
# print(name.upper())#全部变成大写
# li=['w','y','x','s',2,5,0]#里面的数据类型可以各不相同
# print(li,type(li))
# print(li[5])
# print(li[1:6])
# for i in li[1:6]:
#     print(i)
# '''列表和字符串都可以进行迭代'''
# li=['w','y','x','s',2,5,0]
# li.append('shhrez')#整体添加加到最后
# print(li)
# li.extend('shhrez')#分散添加一个一个加进去，也是加到最后
# print(li)
# li.insert(4,'nb')#指定位置添加否则会报错
# print(li)
# li[5]='nb'
# print(li)#修改元素
# print('y' in li)
# print('y' not in li)
# while True:
#     name_list=['bingbing','wangyuxi','hhr']
#     name=input('你的名字是:')
#     if name in name_list:
#         print(f'你的名字{name}已经重复了请重新输入：')
#     else:
#         print(f'这个名字{name}已经被你使用了')
#         name_list.append(name)
#         print(name_list)
#         break
# print(li.index('s',1,5))#你要的东西在哪个一个位置
# print(li.count('6'))#你要的东西重复出现了几次
# li=['w','y','x','s','s',2,5,0]
# del li[2]#指定位置删除
# print(li)
# li.pop()#若无标记位置则默认删除最后一个
# print(li)
# li.pop(5)#指定位置删除
# print(li)
# li.remove('s')#默认删除第一个出现的目标
# print(li)
# while 's' in li:
#     li.remove('s')
# print(li)#利用循环可以删除全部
# li=[1,2,3,56,21,24,20,88]
# li.sort()#从小到大排序
# print(li)
# li.reverse()#直接倒叙
# print(li)
# '''两者一起用可以得到从大到小'''
# '''列表推导式'''
# li=[1,2,2,3,4,9,8]
# [print(i*5) for i in li]
# '''格式为[表达式+for+变量+in+列表]'''
# li=[]
# for i in range (1,11):
#     li.append(i)
# print(li)#与循环相结合
# li=[]
# [li.append(i) for i in range(1,11)]
# print(li)
# '''两者相同的结果，但行数不同'''
# '''格式2[表达式+for+变量+in+列表+if+条件]'''
# '''把奇数放进列表里面'''
# li=[]
# for i in range(1,11):
#     if i%2==1:
#         li.append(i)
# print(li)
# li=[]
# [li.append(i) for i in range(1,11) if i%2==1]
# print(li)
# li=[1,2,3,4,5,[6,7,8],9]
# print(li[5])#[里面的678相当于一个整体一个元素]
# print(li[6])
# print(li[5][2])#2代表的是678里面的2号位置
# tua=(1,2,3,4,5,6,7,8,9)
# print(type(tua))
# tau=(1,)
# print(type(tau))
# '''元组若是只有一个元素记得最后加上逗号'''
# '''元组与列表的区别：元组可查询不可修改，列表都可以'''
# '''可以用index，count，len，tua'''
# print(len(tua))
# print(tua[1:5:2])
#应用的场景：函数的参数和返回值，格式化输出背后的（）就是一个元组，数据不可以被修改时，需要保护数据的时候
#字典
# tua={'name':'bingbing','age':18}
# print(type(tua))
# print(tua)
# tau={'name':'bb','name':'wyx'}
# print(tau)#键不能重复，重复的话第二个覆盖第一个
# tau={'name':'bb','age':'bb'}
# print(tau)#值可以重复
# print(tau['name'])#字典里面没有下标，只能通过键来找
# print(tau['tel'])#用该方法没找到就会报错
# print(tau.get('name','none'))
# print(tau.get('tel','none'))#后面那个是定义找不到之后返回的值
# tau['age']=18
# print(tau)
# tau['tel']=156246
# print(tau)
# tau['tel']=123354
# print(tau)
# '''修改元素若原本有则直接修改，原本没有则新添，若键重复则修改值'''
# del tau['tel']
# print(tau)
# tau.clear()#清空字典里面所有东西但是保留字典
# print(tau)
# tau.pop('name')#指定删除
# print(tau)
# tau.popitem()#默认删除最后一个键
# print(tau)
# tau={'name':'bb','age':'bb'}
# print(len(tau))#有几个键值对
# print(tau.keys())#得到的既不是列表也不是字典
# for i in tau.keys():
#     print(i)
# '''for循环依次取出里面的键'''
# print(tau.values())
# for i in tau.values():
#     print(i)
# '''同理可得只不过这个是取值'''
# print(tau.items())
# for i in tau.items():
#     print(i)
# '''一个一个键值对取出来，i是元组类型'''
# '''运用场景：使用键值对储存一个物体的相关信息'''
# st={1,2,3,4,5,6,7,8,9}
# print(st)#对于整型来说具有顺序
# sty={'a','b','c','d','e','f','g','h','i','j'}
# print(sty)#对于字符串这些来说具有无序性，因为有hash值
# print(hash('a'))
# print(hash('b'))
# print(hash('c'))
# print(hash('d'))
# print(hash('1'))
# print(hash('2'))#加上引号变成了字符串
# print(hash(3))
# print(hash(4))
# '''因为有无序性所以不能修改具有无序性的值'''
# wyx={1,5,13,5,6,2}
# print(wyx)
# '''集合具有去重性，可以去掉重复的'''
# print('原集合：',wyx)
# wyx.add(5)#原本有的就不会再加了
# print('现集合：',wyx)
# wyx.add(8)
# print(wyx)
# wyx.add(5,6)#一次只能添加一个元素
# print(wyx)
# wyx.add((5,6))
# print(wyx)
# wyx={1,2,4,56,4,36}
# wyx.update('567')#update是一个一个拆分之后加入进去的
# print(wyx)
# wyx.update((5,6,7))#update后面必须加可迭代对象如字符串，列表，元组等可以被for循环所使用的
# print(wyx)
# wyx.remove(2)
# print(wyx)
# wyx.pop()
# print(wyx)
# '''默认删除排序后面的第一个元素'''
# wyx.discard(4)
# print(wyx)
# '''与remove的区别是它要是没找到你想要删除的元素不会报错但是remove会'''
# a={1,2,4,3,2,7,64}
# b={5,4,52,6,4,8,4,5,8,2}
# print(a&b)#交集
# '''没有的话返回空集'''
# print(a|b)#并集
# a=1.2
# b=int(a)
# print(b)
# #浮点型转换为整型直接去掉小数留下整数
# a='1234'
# b=int(a)
# print(b)
# '''字符串中只有数字和正负号可以转换字母等其他不可以'''
# age=input('请输入你的年龄')
# age=int(age)
# if age>=18:
#     print('你已经成年了')
# print(float(121))#整型直接加一位直接加一个小数点
# print(float(12.3423))
# '''如果字符串中有正负号，数字和小数点以外的字符，则不支持转换'''
# '''任何类型的数据都可以转换为字符串'''
# n=100
# print(str(n))
# st=1.3000
# print(str(st))
# '''对于小数后面全是0的自动去除但还会留下一位'''
# li=[1,2,4]
# print(str(li))#列表也可以进行转换
# eval#作用：用来执行一个字符串表达式，并返回表达式的值
# print(10+10)#20
# print('10'+'10')#1010
# print('10+10')#10+10
# print(eval('10+10'))#20
# eval可以实行list,dict,tuple,str之间的转换
# str='[[1,2],[2,4],[3,5]]'
# print(type(str))
# li=eval(str)
# print(type(li))
# '''同理可以进行转换上面几种类型'''
# '''生活中不建议用eval，因为不够安全，容易被恶意修改数据'''
# print(list('absjsfd'))
# print(list((1,2,3,4,5)))
# print(list({'name':'wyx','age':18}))
# '''list只适用于可迭代对象，如str，dict，tuple，set，将其转换为列表'''
# '''对于dict来说比较奇特，他只输出键不输出值'''
# li=[1,2,3,4,5]
# li2=li
# print(li)
# print(li2)
# li.append(9)
# print(li)
# print(li2)
# '''赋值，会随着原对象一起改变，等于完全共享资源，一个改变另外一个也会改变'''
# '''浅拷贝：会创建新的对象，拷贝第一层的数据，嵌套层会指向原本的内存地址'''
# import copy#导入copy模块
# li=[1,2,3,4,[5,6,7]]
# li2 =copy.copy(li)
# print(li)
# print(li2)
# print(id(li))
# print(id(li2))
# '''这个时候两个虽然表示出来是一样的但是他们的内存地址是不一样的所以他们不完全相同，但是里面的嵌套列表的地址是相同的'''
# li.append(5)
# print(li)
# print(li2)
# li[4].append(8)
# print(li)
# print(li2)
# '''所以加在嵌套列表里面是一样的'''
# '''优点：拷贝速度快，内存占用少，拷贝效率高，数据半共享'''
# '''深拷贝：相当于完全不共享拷贝，就是拷完之后两个完全不一样，一方怎么改变都不影响另外一方'''
# li=[1,2,3,4,5]
# print(id(li))
# li.append(6)
# print(id(li))
# '''可变类型：变量对应的值可以改变，但是内存地址不会改变'''
# '''常见的类型有：list,dict,set，元组不是'''
# '''同理不可变对象：变量对应的值不可以被修改，如果修改就会生成一个新的值从而分配一个新的内存空间'''
# '''常见类型：数值类型，字符串，元组tuple'''
# '''注意深浅拷贝只针对可变对象对于不可变对象来说不可以用'''
# def wyx():
#     print('你好我是wyx')
#     print('hhr是wyx爹地')
# wyx()
# wyx()
# def wyx():
#     return 'wyx是sb',20
#     return 'nihao'#第二个return及后面的不会返回
# print(wyx())
# '''return后面要是有两个及以上元素返回的时候以元组的形式输出'''
# '''返回值有三个形式1，没有值返回none2，一个的话直接返回3，多个以元组进行返回'''
# '''print和return的区别，return返回计算结果，print打印计算结果，return还有终止的功能'''
# def add(a,b):#里面的a和b是形参就是一个变量还没有被定义
#     return a+b
# print(add(1,2))#1和2是实参去定义a和b给予它赋值
# def funa(name,age,sex):
#     print(name)
#     print(age)
#     print(sex)
# funa('wyx',18,'女')
# '''写了几个就必须传几个，并且有一定的顺序，这个叫必备参数'''
# def funb(b,a=9):
#     print(a)
# funb(344)
# '''def funb(a=9,b):这个是错误的，def funb(b,a=9)这个是对的，所有位置的参数必须出现在默认参数面前，包括函数定义和调用'''
# def func(b,a=9):
#     print(b)
# func(344)
# '''对这种情况344先赋值给b，所以上面那个打印出来是9，下面的是344'''
# '''这个叫默认参数'''
# def fund(*args):#也可以把args改成其他名字，但是args更加符合代码的规范性
#     print(args)
# fund(1,2,3,4,5,6,7,8,9)#以元组的形式接收
# '''这个叫可变参数，传入的值的数量是可以改变的，可以传入多个，也可以不传'''
# def fune(**kwargs):
#     print(kwargs)#以字典的形式进行接收
# fune(name='wyx',age=18)#传输值的时候需要用键值对的形式进行传输
# '''作用：可以拓展函数的功能'''
# def wyx():
#     print('wyx是答辩')
# def hhr():
#     wyx()
#     print('wyx是hhr儿子')
# hhr()
# def study():
#     print('好好学习，天天向上')
#     def nb():
#         print('我要上清北')#不要在内层里面调用外层函数，会陷入死循环，直到超过递归的最大限度
#     nb()#注意缩进，定义和调用是同级的，调用如果在定义里面则无法永远被调用
# study()
# '''这个是嵌套定义，在一个函数里面定义另外一个函数'''
# a=100#全局变量
# def test1():
#     print('这个是1中的值',a)
# def test2():
#     a=120#局部变量
#     print('这个是2中的值',a)
# print('调用函数前a的值',a)#出来是100
# test1()
# test2()
# print('调用函数后a的值',a)#出来是100
# '''局部变量，之所以a没有被覆盖是因为函数内部如果要使用变量，会从函数内部找，有的话就直接使用，没有的话从函数外面找'''
# '''局部变量，只能在被定义的函数中使用，函数外部不能使用'''
# '''作用：在函数内部，临时保存数据，即当函数调用完之后，就销毁局部变量'''
# def test3():
#     num=10
#     print('里面的值是',num)
# def test4():
#     num=20
#     print('里面的值是',num)
# test3()
# test4()
# num=10
# def test3():
#     print('里面的值是',num)
# def test4():
#     global num#声明全局变量
#     num+=1#局部变量
#     print('里面的值是',num)
# print('调用函数前num的值',num)
# test3()
# test4()
# print('调用函数后num的值',num)
# '''总结：global可以对关键字可以对全局变量进行修改，也可以在局部作用域中声明一个全局变量'''
# def outer():
#     a=5
#     def inner():
#         a=10
#         def inner2():
#             nonlocal a#nonlocal只能对上一级的函数进行修改
#             a=15
#             print('inner2中的值',a)
#         inner2()
#         print('inner中的值', a)
#     inner()
#     print('outer中的值', a)
# outer()
# '''切记代码一行一行往下走的'''
# '''匿名函数'''
# add=lambda a,b:a+b
# print(add(3,4))
# '''a,b就是形参，a+b就是返回值的形式'''
# '''lambda的参数形式'''
# #1，无参数
# funa=lambda :'我是wyx'
# print(funa())
# #2,一个参数
# funb=lambda name:name
# print(funb('bingbing'))
# #3，默认参数
# func=lambda name,age=18:(name,age)#最后要以元组的形式输出
# print(func('bingbing'))
# print(func('bingbing',age=200))
# '''默认参数必须写在非默认参数后面'''
# #4,关键字参数
# fund=lambda **kwargs:kwargs
# print(fund(name='bingbing',age=200))
# '''要以键值对输入'''
# '''lambda结合if判断'''
# a=5
# b=6
# print('a比b小') if a<=b else print('a比b大')
# cnm=lambda a,b:'a比b小' if a<=b else 'b比a小'
# print(cnm(a,b))
# '''匿名函数的特点：只能实现简单的逻辑，如果逻辑复杂且代码的量比较大，不建议使用，会降低可读性，后期代码维护更加困难'''
# print(abs(-10))
# print(sum([1,2,3]))
# '''abs是返回绝对值，sum是求和，并且里面只能是可迭代对象，如元组，集合，列表'''
# print(min([1,2,3]))
# print(max([1,2,3]))
# print(min(-5,7,key=abs))#-5
# '''引入key可以进行排序'''
# li={1,2,3,4}
# li2=['a','d','d']
# print(zip(li,li2))
# #1通过for循环
# for i in zip(li,li2):
#     print(i)
# '''元素个数不一致，则按照最短的返回'''
# #2转换成列表打印
# print(list(zip(li,li2)))
# '''注意zip对应的对象都要是可迭代对象'''
# li=[1,2,3,4,5]
# def funa(x):
#     return x*9
# wyx=map(funa,li)
# for i in wyx:
#     print(i)
# print(list(wyx))
# '''映射函数：简单来说就是你选中的可迭代对象都会一一去执行这个函数'''
# li=[1,2,3,4,5]
# funa=lambda x:x*9
# wyx=map(funa,li)
# print(list(wyx))
# from functools import reduce
#
# li2=[1,2,3,4,5]
# def add(x,y):
#     return x+y
# wyx=reduce(add,li2)#它要用到的函数必须是有两个参数的函数，后面那个是可迭代对象
# print(wyx)
# li2=[1,2,3,4,5]
# def add(x,y):
#     return x+2*y
# wyx=reduce(add,li2)
# print(wyx)
# '''reduce：先把对象中的两个元素取出，然后和第三个值进行计算，以此类推'''
# from functools import wraps
#
# tua=[1,2,3,4,5]#拆包
# #方法一
# a,b,c,d,e=tua
# print(a,b,c,d,e)
# '''要求：元组内的元素和接受的个数一样多'''
#方法二
# tua=(1,2,3,4,5)
# a,*b=tua
# print(a,b)#里面的b不要带*
# def funa(a,b,*args):
#     print(a,b,args)#args也是不要带*
#     print(type(args))
# funa(1,2,3,4,5,6)
# '''拆包可以一个一个对应的拆，也可以一级一级的拆'''
# try:
#     print(abh)#一般try下面只有一行代码
# except(NameError,TypeError):#可以选择写要捕获的错位类型，当要多种错误类型时，要元组来表达
#     print('你的代码有问题')
# try:
#     print(abh)
# except Exception as e :#Exception,万能异常，可以捕获任意类型
#     print('你的代码有问题')#as相当于取别名，e是变量名，可以自定义，as e相当于把异常信息保存到变量e中
#     print(e)#打印输出异常的信息
# st=[1,2,3,4,5,6]
# try:
#     print(st[4])
# except Exception:
#     print('你的代码有问题')
# else:
#     print('你很棒')
# st=[1,2,3,4,5,6]
# try:
#     print(st[4])#可能引发异常现象的代码
# except Exception:
#     print('你的代码有问题')#出现异常现象的代码
# else:
#     print('你很棒')#未出现异常现象的代码
# finally:
#     print('继续')#try代码结束后运行的代码无论怎么样都会运行
# '''try和finall可以两个单独使用'''
# '''找寻并且捕获异常'''
# def login():
#     wyx=input('请输入你的密码')
#     if len(wyx)>=6 :
#         return('输入成功')#用return而不用print原因是前者运行的话后面就不会继续运行了，但print不会后面会继续运行所以打123456时成功失败都会出来
#     raise Exception('长度不足六位密码输入失败')
# try :
#     print(login())
# except Exception as e :
#     print(e)
# # '''抛出异常raise，步骤：1，创建一个Exception('xxx')对象,xxx---异常提示信息'''
# # '''2，raise抛出对象(异常对象)，执行了raise代码不会继续往下运行'''
# #模块：本质就是一个py文件，导入一个模块本质上就是执行一个py文件
# #1，内置模块，如：random，time,os,logging等直接导入就可以用了
# #2，第三方模块：下载：cmd窗口输入pip install模块名
# #3，自定义模块，就是自己在项目中定义的模块
# '''注意：命名要遵循标识符规定以及变量的命名规范，并且不要与内置模块起冲突，否则将无法使用'''
# #导入模块
# #1
# import pytest
# print(pytest.name)#变量的导入
# pytest.funa()#函数的导入
# #2
# from pytest import funa,name#导入函数不需要写()，导入你要的东西导入一次就行后面不用再写了
# funa()
# print(name)#如果前面不导入name则无法使用
# from pytest import*#import*代表导入全部内容
# funb()
# '''不过多建议使用from这种方法，有时候起名会有冲突'''
# '''给模块起别名'''
# import pytest as wyx
# wyx.funb()
# print(wyx.name)
# '''给功能取别名'''
# from pytest import funa as a ,name as c ,funb as b
# a()
# print(c)
# '''导入多个功能的时候，用逗号将他们隔开，可以依次取别名'''
# import pytest
# pytest.funb()
# '''if __name__ == '__main__':的用法在要导入的模块里面用他后面的东西将不会被导入进来'''
# #包
# '''含义:就是项目结构中的文件夹/目录'''
# '''与普通文件夹的区别:包是含有_init_.py的文件夹'''
# '''作用:将有联系的模块放到同一个文件夹下,有效避免模块名称冲突问题，让结构更清晰,记住是在文件夹中添加'''
# '''新建包:右键项目名->new->Python Package'''
# '''导包方式一'''
# import hhr
# '''导包方式二'''
# from hhr import hhrnb
# hhrnb.funa()
# '''不建议在init文件中写太多代码,init的作用导入这个包内的其他模块'''
# '''import导入包的时候首先执行init文件'''
# '''_all_ :本质上是一个列表，列表里面的元素就代表要导入的模块,作用:可以控制要引入的东西。'''
# from hhr import hhrnb,login
# hhrnb.funa()
# '''包里可以含包'''
#递归函数
#含义
#如果一个函数在内部不调用其他的函数，而是调用它本身的话，这个函数就是递归函数
#条件
#1.必须有一个明确的结束条件 ---递归出口
#2.每进行更深一层的递归，问题规模相比上次递归都要有所减少
#3.相邻两次重复之间有紧密的联系
# def add():
#     s=0
#     for i in range(1,101):
#         s+=i
#     print(s)
# add()
# '''用递归函数来解决'''
# def add2(n):
#     if n == 1:#明确了结束条件
#         return 1
#     return n+add2(n-1)#因为每进行更深一层的递归，问题规模相比上次递归都要有所减少，所以要n-1
# print(add2(100))
# '''斐波那契数列'''
# def funa(n):
#     if n<=1:
#         return n
#     return funa(n-1) + funa(n-2)
# print(funa(2))
#递归函数优点
#简洁、逻辑清晰、解题更具有思路
#缺点
#使用递归函数的时候，需要反复调用函数，耗内存，运行效率低
#闭包
#条件
#1.函数嵌套(函数里面再定义函数)
#2.内层函数使用外层函数的局部变量
#3.外层函数的返回值是内层函数的函数名
# def outer():#外层函数
#     n=10#外层函数的局部变量
#     def inner():#内层函数
#         print(n)#内层函数使用外层函数的局部变量
#     return inner
# print(outer())#返回的是内部函数的内存地址
# #第一种调用写法
# outer()()#先内后外
# #第二种调用写法
# ot = outer()#调用内函数
# ot()#调用外函数
# def outer(m):#外函数，m是形参，也是外的数的局部变量
#     n=10
#     def inner():
#         print(n+m)
#     return inner#返回函数名，而不是inner()，因为inner函数里面参数比较多时或者说受到限制时，写法不太规范
# ot=outer(30)#调用函数,在这里outer将30传给m，返回的是inner，所以这里ot等于inner
# ot()#调用内函数
#函数引用
# def funa():
#     print(123)
# print(funa)#函数名里面保存了函数所在位置的引用
# a = 1
# print(id(a))
# print(id(1))#a只不过是一个变量名，存的是1这个数值所在的地址，就是a里面存了数值1的引用
# a = 2#修改a,生成了新的值，重新赋值给变量a
# print(id(a))
# print(id(2))
# #在内存地址发生变化，因为值也发生了变量
# def test1():
#     print('这里是wyx')
# test1()
# print(test1)#内存地址(引用)
# te = test1
# te() # 通过引用调用函数
# def outer(m):
#     print(f'outer里面是{m}')
#     def inner(x):
#         print(f'inner里面是{x}')
#         return x+m
#     return inner
# wyx=outer(20)
# print(wyx(35))#20+35
# print(wyx(45))#20+45
# print(wyx(55))#20+55
# #总结:使用闭包的过程中，一旦外函数被调用一次，返回了内函数的引用，虽然每次调用内函数，会开启一个函数，执行后消亡
# #但是闭包变量实际上只有一份，每次开启内函数都在使用同一份闭包变量，所以它不会因为后面赋值而改变前面的赋值
# from sys import set_int_max_str_digits
#
#
# def test():
#     print('发送信息给bb')
# def test2(fn):#这里的fn相当于一个形参
#     print('我是wyx')
#     print('我是hhr')
#     fn()#调入要传输的函数
# test2(test)#这里将test传递给fn
# #装饰器作用:在不改变原有代码情况下额外添加新的功能，装饰器的返回值也是一个函数对象
# #条件:
# #不修改原程序或函数的代码
# #不改变函数或程序的调用方法
# #闭包的三个条件
# #1.函数嵌套
# #2.内函数要使用外函数的局部变量
# #3.外函数的返回值是内函数的函数名
# def send():
#     print('发送信息')
# def outer(fn):
#     def inner():
#         print('登录')
#         fn()
#     return inner
# print(outer(send))
# ot=outer(send)
# ot()
# '''装饰器的原理就是将原有的函数名重新定义为以原函数为参数的闭包'''
# '''语法糖,格式：@被装饰的函数的名字，顶格'''
# def outer(fn):
#     def inner():
#         print('你好')
#         fn()
#     return inner
# @outer#相当于直接把send导入进fn一样省了几行代码
# def send():
#     print('笑死我了')
# send()
# @outer
# def recv():
#     print('我是你爹')
# recv()
# '''被装饰的函数的内函数里面有形参'''
# def outer(fn):
#     def inner(name):
#         print(f'我是{name}')
#         fn(name)
#     return inner
# @outer
# def funa(name):
#     print('这是被装饰的函数')
# funa('bb')#这里的bb是给name赋值
# '''被装饰的函数里面有可变参数*args,**kwargs'''
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)#记住不用加*
# def outer(fn):
#     def inner(*args,**kwargs):
#         print('登录')
#         fn(*args,**kwargs)
#     return inner
# ot=outer(func)#func=fn
# ot('susu',name='bingbing')#给*args，**kwargs输值
# '''susu以元组的形式传递，bingbing以键值对的形式传递'''
#多个装饰器
# def test(fn):
#     def inner():
#         return '你很棒' + fn()
#     return inner
# def test2(fn):
#     def inner():
#         return '你很优秀' + fn()
#     return inner
# @test
# @test2
# def wyx():
#     return '认真学习python'
# print(wyx())#这个时候wyx相当于inner，并且里面的值是'认真学习python'#你很棒你很优秀认真学习python
# '''多个装饰器的过程，距离函数最近的先装饰就这里的test2，由内到外进行'''
#面向对象和面向过程的区别
#面向过程(手洗):需要实现一个功能的时候，着重的是过程，分析出一个个步骤，并把一个个步骤共女用一个个函数实现，再依次去调用一个个函数即可，每一个步骤都需要自己亲力亲为
#面向对象(机洗):需要实现一个功能的时候，看重的是谁去帮我做这件事情(偷懒，找别人帮我做)
#类和对象
#类就是一系列具有相同属性和行为的事物的统称，不是真实存在的事物
#对象是类的具体实现，是类创建出来的真实存在的事物，面向对象思想的核心
#在开发中，先有类，再有对象
#类的三要素
#1，类名
#2，属性:对象的特征描述，用来说明是什么样子的
#3，方法:对象具有的功能(行为),用来说明能够做什么
#举例:
#类名:人类
#属性:身高、体重、年龄
#方法:走路、说话、学习
#创建类
# class Washer:
#     height=800#类属性
#     width=600
# print(Washer.width)#查看类属性:类名.属性名
# Washer.weight=1000
# print(Washer.weight)
# wa=Washer()
# print(wa)#显示对象在内存中的地址
# wa2=Washer()
# print(wa2)
# '''两个结果不一样，说明是不同的对象，可以实例化多个对象'''
#实例方法和实例属性
#实例方法
#由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给se1f
# class Washer:
#     height=6000
#     def wash(self):#self参数是类中的实例方法必须具备的
#         print('我会洗衣服')
#         print('方法中的self',self)#self表示当前调用该方法的对象，在这就是wa
# wa=Washer()#实例化对象
# print(wa)
# wa.wash()#对象调用类中的方法，在这wa就是调用别人的对象
# '''所以print(wa)和print('方法中的self',self)结果是一样的'''
# wa2=Washer()
# print(wa2)
# wa2.wash()
# '''同理wa2和self也是一样的'''
# #self代表对象本身，当对象调用实例方法时python会自动将对象本身的引用作为参数，传递到实例方法的第一个参数se1f里面
# class Person:
#     name='wyx'#类属性
#     def introduce(self):
#         print('我是实例方法')
#         print(f'{Person.name}的年龄：{self.age}')#实例属性,里面的Person换成self也可以
# pe=Person()
# pe.age=18#实例属性
# pe.introduce()
# '''实例属性可以理解为个人特点，类属性可以理解为大家都有的东西'''
# '''实例属性只能由对象名访问不能由类名访问'''
# '''类属性的话两者都可以访问到'''
# #构造函数
# class People:
#     def __init__(self,name,age,height):
#         self.name=name#实例属性
#         self.age=age#age=age这样就不会固定死，如果把后面的age改变就会固定死了
#         self.height=height
#     def paly(self):
#         print(f'{self.name}在打王者')
#     def introduce(self):
#         print(f'{self.name}的年龄是{self.age}身高是{self.height}cm')
# pe=People('wyx',18,170)
# pe.paly()
# pe.introduce()
# pe2 = People('hhr',18,180)
# pe2.paly()
# pe2.introduce()
# #构造函数__init__ ()
# #作用:通常用来做属性初始化或者赋值操作
# #注意:在类实例化对象的时候，会被自动调用
# class Person:
#     def __init__(self):
#         print('我是init函数')
#     def __del__(self):
#         print('我是del函数')
# p=Person()#p=一定要写，实例化对象
# del p#删除这个对象，执行时内存会被立刻回收，会调用对象本身的del方法
# print('这是倒数第二行代码')
# print('这是倒数第一行代码')
# #正常运行时，不会调用del，对象执行结束时，系统才会调用该代码
# #删除对象的时候，解释器会默认调用del方法
# #析构函数，del主要是表示该程序块或者函数已经全部执行结束了
# '''面向对象的三大特性：封装，继承，多态'''
#封装：指的是隐藏对象中一些不希望被外部所访问到的属性或者方法
# class Person:
#     name='wyx'#类属性
#     __age=18#隐藏属性
# pe=Person()
# print(pe.name)
# # print(pe.age)#这种情况会报错，因为age已经被隐藏了
# '''如想要访问被隐藏的东西有两种方法'''
#1
#实际上只是讲他的名字改为_类名__属性名，即_Person__age
# print(pe._Person__age)
#2
#在类的内部访问
# class Person:
#     name='wyx'
#     __age=18
#     def introduce(self):
#         print(f'{Person.name}的年龄是{Person.__age}')
# pe=Person()
# pe.introduce()#比较正规
#4.3私有属性/方法
#1.xxx:普通属性/方法，如果是类中定义的，则类可以在任意地方使用
#2._xxx:单下划线开头，声明私有属性/方法，如果定义在类中，外部可以使用，子类也可以继承，但是在另一个py文件中通过from xxx import *导入时，无法导入
#一般是为了避免与Python关键字冲突而采的命名方法
#3.__xxx:双下划线开头，隐藏属性，如果定在类中，无法在外部直接访问，子类不会继承，井要访问只能通过间接的方式，另一py文件中通过from xxximport *导入的时候，也无法导入
#这种命名一般时python中的魔术方法或属性，都是有特殊含义或者功能的，自己不要轻易定义
# class Person:
#     _name='wyx'
# pe=Person()
# print(pe._name)#这个与双下划线就不一样了
#隐藏方法
# class Man:
#     def __play(self):
#         print('玩手机')
#     def funa(self):
#         print('正常的实例方法')
#         Man.__play(self)#不能漏掉self，在实例方法中调用隐藏的方法
#         self.__play()#更加推荐这样写
# ma=Man()
# ma.funa()
# ma._Man__play()
# #私有方法的话可以参考上面的私有属性一样的殊途同归
# 继承：子类默认继承父类的属性和方法
# 单继承
# class Person:
#     def eat(self):
#         print('我会吃顿饭')
#     def sing(self):
#         print('我会唱歌')
# class Girl(Person):
#     pass#占位符，代码类下面不写任何东西，会自动跳过，不会报错
# girl=Girl()
# girl.eat()
# girl.sing()
# #继承的传递(多重传递)
# class Person:
#     def money(self):
#         print('一百万需要被继承')
# class Man(Person):
#     def money(self):
#         print('我自己有一个亿')
# man = Man()
# man.money()#结果是我自己有一个亿，相当于赋值的说法，所以按后面的准
# '''若想要继承一百万则需要扩展父类的方法'''
# #1
# class Person:
#     def money(self):
#         print('一百万需要被继承')
# class Man(Person):
#     def money(self):
#         Person.money(self)#在这里加入父类的方法，记得写self
#         print('我自己有一个亿')
# man = Man()
# man.money()
# #2，super().方法名()，较为推荐
# #super在python中是一个特殊的类，super是使用super类创建出来的对象，可以调用父类中的方法
# class Person:
#     def money(self):
#         print('一百万需要被继承')
#     def sleep(self):
#         print('我会睡觉')
# class Man(Person):
#     def money(self):
#         super().money()
#         super().sleep()#可以调用父类中任意一个方法
#         print('我自己有一个亿')
# man = Man()
# man.money()
#3，super(子类名，self).方法名()
# class Person:
#     def money(self):
#         print('一百万需要被继承')
#     def sleep(self):
#         print('我会睡觉')
# class Man(Person):
#     def money(self):
#         super(Man,self).money()
#         print('我自己有一个亿')
# man = Man()
# man.money()
# #如果一个类没有继承任何类，则默认继承object类，因此都是新式类
#多继承，继承多个父类
# class Fathrt:
#     def money(self):
#         print('超级有钱')
# class Mother:
#     def appearence(self):
#         print('绝世容颜')
# class Child(Fathrt,Mother):
#     pass
# child = Child()
# child.money()
# child.appearence()
# print(Child.__mro__)#查看他的内置属性，它属于什么类
# #搜索方法时会按照顺序从左向右写出
# #多继承的弊端：代码设计混乱
# class Animal:
#     def eat(self):
#         print('我i会吃饭')
# class Dog(Animal):
#     def eat(self):
#         print('我要吃狗粮')
# class Cat(Animal):
#     def eat(self):
#         print('我要吃猫粮')
# def test(obj):#一个接口实现多个目标
#     obj.eat()
# animal = Animal()
# dog = Dog()
# cat = Cat()
# animal.eat()
# dog.eat()
# cat.eat()
# #test函数传入不同的对象，执行不同的对象的eat函数
# from idlelib.debugger_r import close_subprocess_debugger
#
#
# class Person:
#     name='bingbing'
#     @classmethod
#     def sleep(cls):
#         print(cls.name)
#         print(Person.name)
#         print(cls)#结果和print(Person)是一样的说明了他们两个是相同的，所以cls就是类对象本身，类本质上就是一个对象
#         print('我是wyx')
# print(Person)
# Person.sleep()
# #当方法中需要使用到类对象(如访问私有类属性等)，定义类方法
# #类方法一般是配合类属性使用
# #总结：类属性是公共的，所以方法内部都可以访问到，静态方法不需要访问类属性，因为静态方法和类，对象没有关系
# #实例属性是私有的，只有实例方法内部可以访问的到
# class Person:
#     def __init__(self):
#         print('这是--init--')
#     def __new__(cls, *args, **kwargs):
#         print('我是__new__')
#         print(cls)
#         wyx =super().__new__(cls)
#         return wyx#一定要return,因为它是返回对象引用的
# pe=Person()
# print(pe)
#总结:__init__()和__new__()
#1__new__()是创建对象，__init__()是初始化对象
#2__new__()是返回对象引用，__init__()定义实例属性
#3__new__是类级别的方法，__init__()是实例级别的方法
#2.单例模式
#可以理解成一个特殊的类，这个类只存在一个对象
#优点:可以节省内存空间，减少了不必要的资源浪费
#弊端:多线程访问的时候容易引发线程安全问题共
#方式
#1.通过@classmethod
#2.通过装饰器实现
#3.通过重写__new__()实现(重点)
#4.通过导入模块实现





