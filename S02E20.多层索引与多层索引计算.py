# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:21:45 2022

@author: 15517
"""

# 15.分层索引与计算
# 分层索引：就是在一个轴上拥有多个（两个以上）索引级别，使用户能以低维度形式处理高维度数据
# levels 每个等级上轴标签的唯一值
# labels 以整数来表示每个level上标签的位置
# sortorder 按照指定level的标签名称的字典顺序进行排序（可选参数）
# names  index level的名称
# copy  布尔值，默认为False。 是否拷贝源数据产生新的对象
# verify_integrity 布尔值，默认为True。 检查levels/labels是否持续有效

import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件020/多层索引.xlsx'
data = pd.read_excel(path,index_col=[0,1],sheet_name='有序')
print(data)
print(data.index)
print(data.index.levels[0]) #对应外层索引
print(data.index.levels[1]) #对应内层索引

# 15.1分层索引设置与查询
# 一、index为有序的
data = pd.read_excel(path,index_col=[0,1],sheet_name='有序')
# data = data.set_index('班级','序号') #也可以设置分层索引
data1 = data.loc[('1班',slice(None)),:] #切片筛选index
print(data1)

# 参数
# loc[(a,b),c]中的第一个参数元组为索引内容，a为level0索引对应的内容，b为level1索引对应的内容
# 因为df是一个DataFrame,所以用c来指定列
# slice(None) 是python中的切片操作，这里用来选择任意的id，要注意！ 不能使用':'来指定任意的index
# ':' 用来指定dataframe的任意的列

# 二、index为无序
data = pd.read_excel(path,index_col=[0,1],sheet_name='无序')#设置分层索引
# 数据 = 数据.set_index('课程','得分')  # 也可以这样设置分层索引
# 数据2 = 数据.loc[('语文',slice(None)),:]  # 不能使用这种方法，因为科目是无序的
print(data.index.is_lexsorted()) #检查index是否为无序
# 接下来，我们尝试对Index进行排序。（排序时要在level里指定index名）
data = data.sort_index(level='科目')
data2 = data.loc[('语文',slice(None)),:]
print(data2) #???????????

# 15.2 多层索引的创建的方式【行】
# from_arrays 接收一个多维数组参数，高维指定高层索引，低维指定低层索引
# from_tuples 接收一个元组的列表，每个元组指定每个索引 （高维索引，低维索引）
# from_product 接收一个可迭代对象的列表，根据多个可迭代对象元素的笛卡尔积进行创建索引
# 注：from_product相对于前两个方法而言，实现相对简单，但是，也存在局限

# 1、from_arrays 方法
# from_arrays 参数为一个二维数组，每个元素（一维数组）来分别制定每层索引的内容
import pandas as pd
多层索引 = pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]],names=['x','y'])
print(多层索引)

# 2、from_tuples方法
# from_tuples 参数为一个（嵌套的）可迭代对象,元素为元组类型。元组的格式为：(高层索引内容，低层索引内容)
import pandas as pd
多层索引 = pd.MultiIndex.from_tuples([[('a',1),('a',2),('b',1),('b',2)],names=['x','y']])　
print(多层索引)

# 3、from_product方法
# 使用笛卡尔积的方式来创建多层索引。参数为嵌套的可迭代对象。结果为使用每个一维数组中的元素与其他一维数组中的元素来生成 索引内容。
import pandas as pd
多层索引 = pd.MultiIndex.from_product([['a', 'b'], [1, 2]],names=['x','y'])
print(多层索引)

# 注：如果不在MultiIndex中设置索引名，也可以事后设置
数据.index.names = ['x', 'y']


# 15.3 多层索引的创建的方式 【列】
# 在DataFrame中，行和列是完全对称的，就像行可以有多个索引层次一样，列也可以有多个层次。
import pandas as pd
import numpy as np
index = pd.MultiIndex.from_product([[2019,2020],[5,6]],names=['年','月'])
columns = pd.MultiIndex.from_product([['香蕉','苹果'],['土豆','茄子']],names=['水果','蔬菜'])
data = pd.DataFrame(np.random.random(size=(4,4)),index=index,columns=columns)#笔记3.2
print(data)


# 15.4 分层索引计算
# 多层索引：允许你在一个轴上有多个索引。
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件020/销售.xlsx'
数据 = pd.read_excel(路径,header=[0,1]) # 设置前2行是表头，笔记2.1.2
print(数据.columns)

结果1 = 数据[('土豆', '销量')]+数据[('倭瓜', '销量')] # 通过两层索引相加
print(结果1)

结果2 = 数据['土豆'] +数据['倭瓜'] # 通过第一层索引相加
print(结果2)

总计 = 数据['土豆']+数据['倭瓜']
print(总计) # 单层索引与多层索引无法拼接

总计.columns = pd.MultiIndex.from_product([['合计'],总计.columns])
print(总计)

结果 =pd.concat([数据,总计],axis=1)  # 横向拼接，笔记4.3.3
print(结果)

# MultiIndex 参数表

#设置
# levels 每个等级上轴标签的唯一值
# labels 以整数来表示每个level上标签的位置
# sortorder 按照指定level上的标签名称的字典顺序进行排序（可选参数）
# names index level的名称
# copy 布尔值，默认为False.是否拷贝源数据产生新的对象
# verify_integrity 布尔值，默认为True。检查levels/labels 是否持续有效

# 创建
# from_arrays 接收一个多维数组参数，高维指定高层索引，低维指定低层索引
# from_tuples 接收一个元组的列表，每个元组指定每个索引 （高维索引，低维索引）
# from_product 接收一个可迭代对象的列表，根据多个可迭代对象元素的笛卡尔积进行创建索引

# 获取
# get_level_values  int/name 获取对应级别的索引




























