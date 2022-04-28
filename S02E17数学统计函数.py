# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:45:22 2022

@author: 15517
"""

# 12.数学统计函数
# 数据统计
# df.describe()  查看数据值列的汇总统计
# df.mean()  返回所有列的均值
# df.corr()  返回列与列的相关系数 correlation
# df.count() 返回每一列中的非空值的个数
# df.max()   返回每列的最大值
# df.min()
# df.median()  中位数
# df.std()    标准差
# sum; mad 平均绝对方差 mean absolute deviation ;
# argmin 最小值的索引位置; idxmin 每列最小值的行索引
# mode;abs;std;var;sem 标准误 standard erroe of the mean
# skew 偏度; kurt 峰度; quantile 分位数; cumsum 累计和; cumprod 累积积
# cummax 累积最大值; cov() 协方差; corr() 相关系数; rank 排名; 
# pct_change() 时间序列变化

import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件017/数据统计.xlsx'
data = pd.read_excel(path,index_col='序号')
print(data.head())
print(data.describe()) #所有数值列
print(data['语文'].describe()) #只看一列




















