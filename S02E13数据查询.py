# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:42:37 2022

@author: 15517
"""

#　查询数据   loc
# 8.1 单条件查询
# 语法： loc[行标签，列标签]
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件013-014/筛选.xlsx'
data = pd.read_excel(path,index_col='出生日期')
print(data.loc['1983-10-27','语文'])

# 8.2多条件查询
print(data.loc['1983-10-27',['语文','数学','英语']])
# 同理：行也可以通过列表查询几个日期

# 8.3 使用数据区间范围进行查询
print(data.loc['1983-10-27':'1990-12-31',['语文','数学','英语']])

# 8.4 使用条件表达式进行查询
print(data.loc[(data['语文']>60)&(data['英语']<60),:])  #  ,: 表示 列取全部

# 8.5 loc实现条件判断
import pandas as pd
import datetime as dt
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件013-014/条件判断.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data)

data.loc[data['性别'] == "男",'称呼'] = "先生"
data.loc[data['性别'] == "女",'称呼'] = "女士"




























