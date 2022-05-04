# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:21:58 2022

@author: 15517
"""

# map,apply,applymap

# 在数据处理中，经常会对一个DataFrame进行逐行、逐列和逐元素的操作
# 对应这些操作，PD中的map\apply\applymap可以解决绝大部分的数据处理需求

# 24.1 map
# 不管是利用字典还是函数进行映射，都是把对应的数据逐个当作参数传入字典或函数中，得到映射后的值

import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/数据.xlsx'
data = pd.read_excel(path)
# 方法1：使用字典进行映射
data['性别'] = data['性别'].map({'男':'先生','女':'女士'})
# 方法2：使用函数
def 替换(x):
    称呼 = '先生' if x == '男' else '女士'
    return 称呼
data['性别'] = data['性别'].map(替换)
print(data)

# 24.2 apply
# 一、Series数据处理
# apply与map的区别：能够传入功能更为复杂的函数
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/数据.xlsx'
data = pd.read_excel(path)
def 修改分数(x,误差值): #第一个参数代表该函数处理的每一个元素，第二个参数args是传入的参数
    return x + 误差值
# 以元组的方式传入额外的参数
data['语文'] = data['语文'].apply(修改分数,args=(10,))# (10,)表示一个参数
print(data)


# 二、DataFrame 数据处理
# 行标签是0轴，列标签是1轴，axis=0沿着0轴，axis=1沿着1轴
import numpy as np
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/数据.xlsx'
data = pd.read_excel(path)
data1 = data[['语文','数学','英语']].apply(np.mean,axis=0)
data2 = data[['语文','数学','英语']].apply(np.sum,axis=1)
print(data1)
print(data2)


data['总分'] = data2
print(data)
删除_身高 = data.身高
删除_体重 = data.体重
data = data.drop(['身高','体重'],axis=1)
data.insert(6,'身高',删除_身高)
data.insert(7,'体重',删除_体重)
print(data)


path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/数据.xlsx'
data = pd.read_excel(path)
def BMI(data):
    身高 = data['身高']
    体重 = data['体重']
    BMI = 体重/身高 **2
    return BMI
data['BMI'] = data.apply(BMI,axis=1)
print(data) 

# 当axis设置了axis=1对行进行操作时，会默认将每一行数据以Series的形式（Series的索引为列名）传入指定函数，返回相应的结果

# 24.2 applymap
# 它的用法非常简单，会对DataFrame中的每个单元格执行指定函数的操作，虽然用途不如apply广泛，但在某些场合下还是比较有用：
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/数据2.xlsx'
data = pd.read_excel(path)
data2 = data.applymap(lambda x:"%.3f" % x) #数据改为保留三位小数显示
print(data2)







