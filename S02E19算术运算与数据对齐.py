# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:58:55 2022

@author: 15517
"""

# 算数运算无非就是加减乘除，但是需要注意2点：
# 空值与数字进行计算，结果是空值！
# 对除数为0的处理：
# 1/0 = inf       无穷大
# -1/0 = -inf    负无穷大
# 0/0 = Nan
#

# 处理空值
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件019/计算.xlsx'
data = pd.read_excel(path)
print(data.head())
result = data['1店'] + data['2店']
print(result)

# 方法1 ： 将空值填充为0
result = data['1店'].fillna(0) + data['2店'].fillna(0)
print(result)

# 方法2 : 灵活算数法
result = data['1店'].add(data['2店'],fill_value=0)
print(result)

# 方法 反转方法 描述
# add  radd    加法
# sub  rsub    减法
# div  rdiv    除法
# floordiv rfloordiv 整除
# mul  rmul    乘法
# pow  rpow    幂次方

# 处理inf无穷大
result = data['1店'].div(data['2店'],fill_value=0)
print(result)

# 如果想将inf或-inf当成nan值
import pandas as pd
pd.options.mode.use_inf_as_na = True
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件019/无穷大.xlsx'
数据 = pd.read_excel(路径)
结果 = 数据['1店'].div(数据['2店'],fill_value=0)
print(结果)


# 数据对齐
# 数据对齐：是数据清洗的重要过程，可以按索引对齐进行运算，如果没对齐的位置则补NaN，最后也可以填充NaN
# 在Excel通常是先Vlookup然后再加减乘除，Pandas省去了这个过程，直接计算
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件019/对齐.xlsx'
数据1 = pd.read_excel(路径,index_col='序号',sheet_name='Sheet1')
数据2 = pd.read_excel(路径,index_col='序号',sheet_name='Sheet2')
结果 = 数据1.add(数据2,fill_value=0)
print(结果.fillna(0))










