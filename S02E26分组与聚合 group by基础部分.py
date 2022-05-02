# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:33:16 2022

@author: 15517
"""

# groupby分为三个步骤：拆分-应用-合并
# DataFrame可以在其行（axis=0）或列（axis=1）上进行分组。
# 然后，将一个函数应用到各个分组并产生新值。
# 最后，所有这些函数的执行结果会被合并到最终的结果对象中去。
# GroupBy的size方法可以返回一个含有分组大小的Series。

# 20.1 对分组进行迭代【遍历各分组】
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合.xlsx'
data = pd.read_excel(path)
print(data.head())
for (i,j),group in data.groupby(['城市','区']):
    print(i) # 城市分组
    print(j) # 区分组
    print(group) #城市和区的分组

# 20.2 分组聚合
print(data.head())
data1 = data.groupby(['城市','区'])[['人数']].sum()
print(data1)
data1.to_excel('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合.xlsx')


data2 = data.groupby(['城市','区'])[['人数','金额']].sum()
print(data2)
data2.to_excel('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/1.xlsx')

path1 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合2.xlsx'
data3 = pd.read_excel(path1,index_col='店号')
# 不同列的不同计算方法
dict = {'1月':'count','2月':sum,'3月':max,'4月':'mean'}
data4 = data3.groupby('店号').agg(dict)
print(data4)

# 注意：
# 如果按一列聚合，只传列名字符串，如果多个就要传由列名组成的列表
# 聚合方法可以使用 Pandas 的数学统计函数 或者 Numpy 的统计函数
# 如果是 python 的内置统计函数，直接使用变量，不需要加引号

# 20.2.1 agg函数
# agg函数一般与groupby配合使用，agg是基于列的聚合操作，而groupby是基于行的
# DataFrame.agg(func,axis=0,*args,**kwargs)
# func ：函数，函数名称，函数列表，字典{'行名/列名','函数名'}
# 使用指定轴上的一个或多个操作进行聚合


# 20.3 使用字典和Series分组
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合2.xlsx'
data = pd.read_excel(path,index_col='店号')
对应关系 = {'1月':'一季度','2月':'一季度','3月':'一季度','4月':'二季度'}
data2 = data.groupby(对应关系,axis=1)
print(data2.sum())

# 20.4 通过函数分组【不常用】
# eg1:按城市名称的字数进行分组聚合
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合.xlsx'
data = pd.read_excel(path,index_col='城市')
data1 = data.groupby(len).sum()
print(data1)

path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合2.xlsx'
data = pd.read_excel(path,index_col='店号')
S1 = ['北京','北京','北京','北京','天津','天津']
data2 = data.groupby([len,S1]).min()
print(data2)


# 20.5 通过索引级别分组
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合3.xlsx'
data = pd.read_excel(path,index_col=[0,1])
data3 = data.groupby(level='班级').mean()
print(data3)

path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件026/分组聚合4.xlsx'
data = pd.read_excel(path,header=[0,1])
L1 = ['1季度','1季度','1季度','2季度','2季度']
L2 = ['1月','2月','3月','4月','5月']
多层索引 = pd.MultiIndex.from_arrays([L1,L2], names=['季度','月份']) #笔记15.2
data2 = pd.DataFrame(data,columns=多层索引)
data3 = data2.groupby(level='季度',axis=1).sum()
print(data3)

































