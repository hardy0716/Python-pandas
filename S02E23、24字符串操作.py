# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:21:50 2022

@author: 15517
"""

# 18.1 字符串对象方法

# 例如：36℃把36分割出来，并转成整形
数据['温度'].str.replace('℃','').astype('int64')

# 18.1.1 cat和指定字符进行拼接
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件023-024/字符串.xlsx'
data = pd.read_excel(path)
print(data.head())
print(data['姓名'].str.cat()) # 不指定参数，所有姓名拼接

print(data['姓名'].str.cat(sep='、')) 

print(data['姓名'].str.cat(['变身']*len(data)))
# ['变身'] * len(数据) 相当于 ['变身'] * 6次

print(data['姓名'].str.cat(['变身']*len(data),sep='^'))

print(data['姓名'].str.cat(['变身']*len(data),sep='^',na_rep='@'))
# 如果一方为NaN,结果也为NaN,因此我们可以指定na_rep,表示将NaN用na_rep替换

data0 =[['王一','男','学生'],['张二','男','经理'],['李三','女','教师'],['赵四','女','画家']] 
data = pd.DataFrame(data0,columns=['姓名','性别','身份'])

data['合并1'] = data['姓名']+data['性别']+data['身份']
print(data)

# 等价于以下语句,可以加sep参数分隔符
#但是注意哦，只能应用于series，不能使数据Dateframe！
data['合并2'] = data['姓名'].str.cat(data['性别'],sep=',').str.cat(data['身份'],sep=',')
print(data)

# 18.1.2 split 按照指定字符串分隔
data = pd.read_excel(path)
print(data['状态'].str.split())  #不指定分隔符，就是一列表
print(data['状态'].str.split('血')) # 和python内置split一样
print(data['状态'].str.split('血',n=-1)) # 指定n，表示分隔次数，默认是-1，全部分隔
print(data['状态'].str.split('血',expand=True))
# 注意这个expand，默认是False，得到是一个列表
# 如果指定为True，会将列表打开，变成多列，变成DATAFrame
# 列名则是按照0 1 2 3····的顺序，并且默认Nan值分隔后还是为Nan
# 如果分隔符不存在，还是返回DATAFrame

#rsplit 和 split用法一致，只不过默认是从右往左分隔


# 18.1.3 partition按照指定字符分割
print(data)
print(data['状态'].str.partition('血'))
# partition只会分隔一次
# 第一个元素：第一个分隔符之前的部分
# 第二个元素：分隔符本身
# 第三个元素：第一个分隔符之后的内容
# 如果有多个分隔符，也只会按照第一个分隔符分隔
print('BbBbB'.partition('b'))

print((data['状态'].str.partition('平')))
print(data['状态'].str.partition())
# 上面两个情况结果是一样的
# rpartition和partition类似，不过是默认是从右往左找到第一个分隔符


# 18.1.4 get获取指定位置的字符，只能获取1个
print(data['状态'].str.get(2)) #获取指定索引的字符，只能传入int
# 如果越界，返回Nan

# 18.1.5 slice 获取指定范围的字
# slice 和 python内置的slice一样。 get相当于是[n],slice相当于是[m:n]

print(data['状态'].str.slice(0))# 指定一个值的话，相当于[m:]
print(data['状态'].str.slice(0,3)) # 相当于[m:n],从0开始不包括3
print(data['状态'].str.slice(0,3,2)) # 相当于[m: n: step]
print(data['状态'].str.slice(5,9,2)) # 索引越界，默认为空字符串，原来Nan还是Nan

# 18.1.6 slice_replace 筛选出来之后替换
print(data['状态'].str.slice_replace(1,3,"520"))
# 将slice为[1:3]的内容换成"distance"，既然替换，所以这里不支持步长。


# 18.1.7 join将每个字符之间使用指定字符相连
# 相当于 sep.join(list(value))

print(data['状态'].str.join('a'))


# 18.1.8 contains 判断字符是否含义指定子串，返回的是bool类型
print(data['状态'].str.contains('血'))  # NaN还是返回Nan
print(data['状态'].str.contains('血',na=False))
print(data['状态'].str.contains('血',na=True))
print(data['状态'].str.contains('血',na="没有"))


# 18.1.9 startswith 是否某个子串开头
print(data['状态'].str.startswith('满'))
# NaN 还是返回NaN，可以按照na=False或na=True替换

# 18.1.10 endswith 判断是否以某个子串结尾
print(data['状态'].str.endswith('满'))


# 18.1.11 repeat重复字符串
print(data['姓名'].str.repeat(3)) #把姓名重复3次

# 18.1.12 pad将每一个元素都用指定的字符填充，记住只能是一个字符
print(data['姓名'].str.pad(5,fillchar='&')) 
# 表示要占5个字符，用'&'填充，默认左填充
print(data['姓名'].str.pad(5,fillchar='<',side='right'))
# 表示要占5个字符，用'<'填充，右填充
print(data['姓名'].str.pad(5,fillchar='<',side='both'))
# 指定side为both，会在两端填充

# pad 的变化
# center(5, fillchar="<")   <==>   pad(5, side="both", fillchar="<")
# ljust(5, fillchar="<")   <==>   pad(5, side="right", fillchar="<")
# rjust(5, fillchar="<")   <==>   pad(5, side="left", fillchar="<")

# 18.1.13 zfill填充，只能是0,从左边填充  zero fill
print(data['姓名'].str.zfill(10))

# 18.1.14 encode编码，decode解码
print(data["attack"].str.encode("utf-8"))
print(data["attack"].str.encode("utf-8").str.decode("utf-8"))


# 18.1.15 strip按照指定内容,从两边去除
print(data['里程'].str.strip('中远近离'))
# lstrip rstrip 类别python字符串的lstrip和rstrip

# 18.1.16 get_dummies
print(data['里程'].str.get_dummies('距'))
# 按照“距”进行分割，得到列表
# 所有列表中的元素共有“中远,近,远,离”四种

# 18.1.17 translate 指定部分替换
dict = str.maketrans({'距':'ju','离':'li'})
print(data['里程'].str.translate(dict))


# 18.1.18 find 查找指定字符第一次出现的位置
print(data['日期'].astype('str').str.find("-"))
# 当然可以指定范围,包括起始和结束
print(data["日期"].astype('str').str.find("-", 5))
print(data["日期"].astype('str').str.find("我")) #找不到返回-1

# rfind和find类似，不过是从右往左查
# index和find类似，但是找不到就报错
# rindex和rfind类似，但是找不到就报错


# 18.1.19 字母大小写
print(data.str.lower())  # 所有字符转成小写
print(data.str.upper())  # 所有字符转成大写
print(data.str.title())    # 每一个单词的首字母大写
print(data.str.capitalize()) # 第一个字母大写
print(s.str.swapcase())  # 大小写交换

# 18.1.20 判断【返回T或F】
print(data.str.isalpha()) # 是否全是字母
print(data.str.isnumeric()) # 判断是否全是数字
print(data.str.isalnum()) # 判断是否全是字母或者数字

# isdecimal只能用于Unicode数字
# isdigit用于Unicode数字，罗马数字
# isnumeric用于unicode数字，罗马数字，汉字数字
# 总的来说，isnumeric最广泛，但是实际项目中，一般很少会有这种怪异的数字出现
# 如果只是普通的阿拉伯数字，那么这三个方法基本上是一样的，可以互用

print(s4.str.isspace()) # 判断是否全是空格
print(s5.str.islower()) # 判断是否全是小写
print(s5.str.istitle()) # 判断每个单词的首字母是否是大写(其他字母小写)


# 18.2 正则表达式
# 18.2.1 match 是否匹配给定的模式
# match 和python正则中的match一样，是从头开始匹配的。返回布尔型，表示是否匹配给定的模式
print(data['状态'].str.match(".{2}激"))
# NaN还是返回Nan，可按照 na= False 或 na = True 替换

# 18.2.2 extract 分组捕获
import re
print(data["日期"].astype('str').str.extract("\d{4}-(\d{2})-(-d{2})"))

# 18.2.3 replace 替换
# 关于replace替换详细的内容请看16.数据替换
print(data["日期"].astype('str').str.replace("(\d+)-(\d+)-(\d+)", r"\3/\2/\1"))
# 这里面的replace是支持正则的。
# 并且一般我们会加上r表示原生的，这是在正则中
# 对于pandas来说，第一个参数是不需要加的，如match。但是第二个参数是要加上r的
# 尤其是分组替换，但如果只是简单字符串替换就不需要了。








