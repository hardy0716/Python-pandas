# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:34:03 2022

@author: 15517
"""

# 22.数据透视表 pivot_table

# pivot_table(data, values=None, index=None, columns=None,aggfunc='mean', 
#             fill_value=None, margins=False, dropna=True, margins_name='All')

# pivot_table有四个最重要的参数index、values、columns、aggfunc

# 在需要多个groupby 的时候，可以优先考虑此函数

# 1、index需要聚合的列名，默认情况下聚合所有数据值的列
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件028-029/透视.xlsx'
data = pd.read_excel(path)
print(data.head())
data1 = pd.pivot_table(data,index=['部门','销售人员'])
print(data1)


# 2、values 在结果透视的 行上 进行分组的列名或其他分组键【就是透视表里显示的列】
data2 = pd.pivot_table(data,index=['部门','销售人员'],values=['数量','金额'])
print(data2)

# 3、columns 在结果透视表的 列上 进行分组的列名或其他分组键
data3 = pd.pivot_table(data,index=['部门','销售人员'],values=['数量','金额'],columns='所属区域')
print(data3)

# 4、Aggfunc聚合函数或函数列表(默认情况下是mean) 可以是groupby里面的任意有效函数
import pandas as pd
import numpy as np
data4 = pd.pivot_table(data,index=['部门','销售人员'],values=['数量','金额'],columns='所属区域',aggfunc=[sum,np.mean])
print(data4)


# 5、fill_value 在结果表中替换缺失值
# 例如： fill_value = 0

# 6、dropna 如果为True,将不含所有条目均为Name的列(默认为False)
# dropna = True

# 7、margins 添加行/列小计和总计 (默认为False)
# margins = True
# 不是简单地求和，而是与 aggfunc 的规则相同,为True时会添加行/列的总计.


# 22.1 交叉表 crosstab
# 是透视表的一部分，aggfunc = count而已
# pd.crosstab(data.Nationality,data.Handedness,margins = True)

# 例如：根据日期中的月份和所属区域，对部门进行统计(计数)
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件028-029/透视.xlsx'
data = pd.read_excel(path)
data1 = pd.crosstab([data.日期.dt.month,data.所属区域],data.部门,margins=True)
print(data1)
data1.to_excel('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件028-029/123.xlsx')


















