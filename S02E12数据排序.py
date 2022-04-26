# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 15:53:57 2022

@author: 15517
"""

# 一、排序
# 对Series数据进行排序
# series.sort_values() 与 sort_index() 分别按照值、索引进行排序
# ascending 参数默认为True，对values升序排序
# inplace参数默认为False，当指定inplace=True时，将同时修改元数据

# 对DataFrame数据进行排序
# Dataframe也有按sort_values（）与 sort_index（）分别按照值、索引进行排序。
# 参数by=“columns_name”指定排序值参考列，默认ascending=True按升序排序,
# 指定inplace=True,将同时修改原数据 

#　DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last') 
# 参数说明
# axis：如果axis=0，那么by="列名"；如果axis=1，那么by="行号"；  
# ascending:True则升序，可以是[True,False]，即第一字段升序，第二个降序  
# inplace=True：不创建新的对象，直接对原始对象进行修改；
# inplace=False：对数据进行修改，创建并返回新的对象承载其修改结果。

# kind:排序方法，{‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’
# na_position : {‘first’, ‘last’}, default ‘last’，默认缺失值排在最后面  

#　例1：按语文分数降序排列
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件012/排序.xlsx'
data = pd.read_excel(path,index_col='序号')
data.sort_values(by='语文',inplace=True,ascending=True)
data1 = data.sort_values(by='语文',inplace=False,ascending=False)
print(data)
print(data1)


# 例2：按语文分数排序降序，数学升序，英语降序
data.sort_values(by=['语文','数学','英语'],inplace=True,ascending=[False,True,False])
print(data)


# 例3：按索引进行排序
data.sort_index(inplace=True)
print(data)


# 7.2排序进阶篇
import pandas as pd
path1 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件012/排序进阶.xlsx'
data2 = pd.read_excel(path1)
data2.sort_values(by='a',inplace=True,ascending=False)
print(data2)

data2.sort_values(by=1,inplace=True,ascending=False,axis=1)
print(data2)





















