# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:50:05 2022

@author: 15517
"""

# 重复数据的处理
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件018/去重.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data.head())
print(data['姓名'].unique()) # 唯一值，以一个列表形式出现
print(data['姓名'].value_counts()) #姓名出现过几次

# 删除重复值
# DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
# subset：用来指定特定的列，默认是所有列
# 	keep：指定处理重复值的方法： 
# 	     first：保留第一次出现的值
# 	     last：保留最后一次出现的值
# 	     False：删除所有重复值，留下没有出现过重复的
print(data.drop_duplicates(subset=['姓名'],keep='first'))

# 提取重复
# DataFrame.duplicated(subset=None, keep='first')
print(data.duplicated())  # 判断重复行
print(data.duplicated(subset='姓名')) #判断某列重复数据
dup = data.duplicated(subset='姓名')
print(data[dup])  #  提取重复








