# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:30:53 2022

@author: 15517
"""

# 前面使用fillna填充缺失值属于特殊案例
# replace(): 替换
# 字符串序列.replace(旧子串，新子串，替换次数)
# 注意: 如果替换次数超过了子串出现次数，就替换所有子串。省略替换次数就是全部替换

v = "你好，世界！ ^你好，中国！ ^我们一起学习中国话！ ^中国加油！"
print(v.replace('中国','祖国'))
print(v.replace('中国', '祖国',2))
print(v.replace('中国','祖国',10))
print(v)  # 字符串未被修改

# 16.1替换全部或者某一行
# 一、整个表全部替换
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件021/替换.xlsx'
data = pd.read_excel(path)
print(data)
data.replace('城八区','海淀区',inplace=True)
print(data)

# 二、某一行替换
data = pd.read_excel(path)
data['城市2'].replace('城八区','海淀区',inplace=True)
print(data)

# 16.2 替换指定的某个或多个数值（用字典的形式）
data = pd.read_excel(path)
dict = {'A':20,'B':30}
data.replace(dict,inplace=True)
# 字典里的键作为原值，字典里的值作为替换的新值

# 也可以用列表的形式
data = pd.read_excel(path)
data.replace(['A','B'],[20,30],inplace=True)
print(data)

# 进阶：如果想要替换的新值一样的话
data = pd.read_excel(path)
data.replace(['A','B'],30,inplace=True)
print(data)


# 16.3 替换某个数据部分内容
data = pd.read_excel(path)
data['城市'] = data['城市'].str.replace('城八','市')
print(data)

# 16.4 正则表达式替换
data = pd.read_excel(path)
data.replace('[A-Z]',88,regex=True,inplace=True)  #笔记9.2
print(data)



















