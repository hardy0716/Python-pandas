# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:09:59 2022

@author: 15517
"""

# 21.1 isin()接收一个列表,判断该列中元素是否在列表中
# isin()的逆函数
# 在前面加上~，其他用法同上

# 21.2 Pandas函数的应用
# 要将自定义或其他库的函数应用于Pandas对象，有三个重要方法。
# 使用适当的方法取决于函数是否期望在整个DataFrame行或列元素上进行操作

# 表式函数应用
# pipe()
# 可以通过将函数和适当数量的参数作为管道参数来执行自定义操作，从而对整个DataFrame执行操作

# 行列函数应用
# apply()
# 沿DataFrame或Panel的轴应用任意函数，与描述性统计一样，apply()方法使用一个可选的axis参数

# 元素函数应用
# applymap()
# 和Series上的map()类似，接收任何Python函数，要求能够接收单个值并返回单个值


# 21.3 案例
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件027/分组.xlsx'
data = pd.read_excel(path)
print(data.head())

# 按索引的奇偶行分组
data1 = data.groupby(data.index%2 == 0)[['语文','数学','英语']].sum()
print(data1)

# 按前后5个分组
data2 = data.groupby(data.index>=5)[['语文','数学','英语']].sum()
print(data2)

# 按姓氏或首字母分组
data3 = data.groupby(data.姓名.str[0])[['语文','数学','英语']].sum()
print(data3)

# 按姓名第1和第2个字或第1和第2个字母分组，注意两个str要写在列表中
data4 = data.groupby([data.姓名.str[0],data.姓名.str[1]])[['语文','数学','英语']].sum()
print(data4)

# 按指定班级分组 (不需要全部班级时使用)
data5 = data.groupby(data.班级.isin(['1班','2班']))[['语文','数学','英语']].sum()
print(data5)

# 按指定班级分组(不包括1班和2班的其它班级，记住~加的位置，没有isnotin函数）)
data6 = data.groupby(~data.班级.isin(['1班','2班']))[['语文','数学','英语']].sum()
print(data6)

# 按日期小时分组
data7 = data.groupby([data.时间.dt.date,data.时间.dt.hour])[['语文','数学','英语']].sum()
print(data7)

# 按日期中的年份分组
data8 = data.groupby([data.时间.dt.year])[['语文','数学','英语']].sum()
print(data8)

# 利用表格函数pipe直接使用分组方法
data9 = data.pipe(pd.DataFrame.groupby, '班级').sum()
print(data9)






































