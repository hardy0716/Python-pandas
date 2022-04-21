# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:06:10 2022

@author: 15517
"""

# DataFrame  二维数据，整个表格，多行多列 简称df
# df.index   索引列
# df.columns  列名
# Seies       一维数据，一行或者一列

#Series是一种类似于一维数组的对象，
#它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成
import pandas as pd
#3.1.1 仅有数据列表即可产生最简单的Series
数据 = pd.Series([520,'孙兴华',1314,'2022-04-21'])
# 左侧是索引，右侧是数据
print(数据)
print(数据.index) #获取索引，返回索引的（start, stop, step）
print(数据.values) # 获取数据值，返回值序列，打印元素值的列表


# 3.1.2 我们指定Series的索引
数据1 = pd.Series([520,'孙兴华',1314,'2022-4-21'],index=['a','b','c','d'])#指定索引
print(数据1)
print(数据1.index)

# 3.1.3 使用Python字典创建Series
dict = {'name':'孙兴华','性别':'男','age':20,'address':'花果山'}
data = pd.Series(dict)
print(data)
print(data.index)

# 3.1.4 根据标签索引查询数据
print(data)                 #查询整个字典
print(data['name'])         #通过key可以查询对应的值
type(data['age'])           #通过key可以查询值对应的类型
print(data[['name','age']])   #通过多个key查对应的值
type(data[['name','age']])    #注意：不返回值的类型，而返回Series     pandas.core.series.Series


# 3.1.5 键和值存在两个列表中，创建Series
col1 = ['姓名','性别','年龄']
col2 = ['孙兴华','男',20]
data1 = pd.Series(col2,index=col1) #指定col1为索引
print(data1)

# Series只是一个序列，可能是一行，也可能是一列，现在无法确定
# 用行的方法，把Series加入DataFrame，就是行，反之就是列。

# Series的常用方法
数据.index #查看索引
数据.values #查看数值
数据.isnull() #查看为空的，返回布尔型
数据.notnull() 
数据.sort_index() #按索引排序
数据.sort_values() #按数值排序

路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件006/数据结构.xlsx'
读取数据 = pd.read_excel(路径,header=None,names=['序号','姓名','年龄','电话','地址','入职日期'],index_col='序号')
print(读取数据)
print(读取数据.index)           #查看索引
print(读取数据.values)          #查看数值
print(读取数据.isnull())        #查看是否为空
print(读取数据.notnull())       #查看是否为空
print(读取数据.sort_index())    #按照索引排序
print(读取数据.sort_values('入职日期')) #按数值排序















