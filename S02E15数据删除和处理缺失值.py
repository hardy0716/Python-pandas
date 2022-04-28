# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:55:22 2022

@author: 15517
"""

# 10.1数据删除drop函数
# 一、删除DataFrame的某行或某列数据
# 1.删除某行或某列的数据可以使用pandas提供的drop
# 2.drop(labels, axis=0, level=None, inplace=False, errors='raise')
# axis=0表示删除行，axis=1表示删除列
# 3.参数
# labels 接受string或array。 代表删除的行或列的标签，无默认
# axis 接受0或1. 默认为0
# levels 接受int或者索引名 代表标签所在级别，默认为None
# inplace 接收boolean  代表操作是否对原数据生效。默认为False

# 10.1.1 drop函数
# 删除行
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件015-016/删除.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data.head())
print(data.drop(2))  #删除单行，直接写行标签
print(data.drop(labels=[1,3]))# 删除多行，使用labels，标签写成列表

# 删除列
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件015-016/删除.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data.head())
print(data.drop('语文',axis=1)) # 删除单列
print(data.drop(labels=['语文','数学'],axis=1)) # 删除多列

# 10.12 drop中 inplace参数
# 注意：凡是会对原数组作出修改并返回一个新数组的，往往都有一个 inplace可选参数。如果手动设定为True（默认为False），那么原数组直接就被替换。
# 而采用inplace=False之后，原数组名对应的内存值并不改变，需要将新的结果赋给一个新的数组或者覆盖原数组的内存位置。

import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件015-016/删除.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data.head())
data.drop(labels=['语文','数学'],axis=1,inplace=True)
print(data)

print(data.drop(labels=['语文','数学'],axis=1))
print(data)


# 10.2 查看缺失值
data = pd.read_excel(path,index_col='序号')
print(data.isnull())        # 是缺失值就显示为T
print(data.notnull())    # 不是缺失值就显示为T

# 10.3 缺失值的处理、
#DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

# how: 与axis配合使用
# how=‘any’ :只要有缺失值出现，就删除该行或列
# how=‘all’:  所有的值都缺失，才删除行或列


# thresh： axis中至少有thresh个非缺失值，否则删除
# 比如 axis=0，thresh=10：标识如果该行中非缺失值的数量小于10，将删除这一行
# subset: list


# 在哪些列中查看是否有缺失值
# inplace: 是否在原数据上操作。如果为真，返回None，否则返回新的copy，去掉了缺失值

print(data.dropna())  #删除所有有空值的行
print(data.dropna(axis=1)) #删除有空值的列
print(data.dropna(how='all')) #删除所有值为Nan的行
print(data.dropna(thresh=2)) #至少保留两个非缺失值
print(data.dropna(subset=['语文','数学'])) # 在哪些列表中查看

# 10.3.2  将缺失值用某些值填充（0，平均值，中值等）
# DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)
# value:  scalar, dict, Series, or DataFrame
# dict 可以指定每一行或列用什么值填充
# method： {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None
# 在列上操作

# ffill / pad: 使用前一个值来填充缺失值
# backfill / bfill :使用后一个值来填充缺失值
# limit 填充的缺失值个数限制

# 10.3.3 填充常数
print(data.fillna(0)) #用常数填充
print(data.fillna({'语文':0.1,'数学':0.2,'英语':0.3}))# 通过字典填充不同的常数

# 10.3.4 填充方式
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件015-016/填充.xlsx'
data1 = pd.read_excel(path)
print(data1.head())
print(data1.fillna(method='bfill'))
# 如果轴变了，左和右就变成了前和后

# 10.3.5 限制填充数量
print(data1.fillna(method='ffill',limit=1))









