# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:59:00 2022

@author: 15517
"""

import pandas as pd 
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件028-029/Vlookup.xlsx'
data1 = pd.read_excel(path,sheet_name='花名册')
data2 = pd.read_excel(path,sheet_name='成绩单')
result = pd.merge(data1,data2.loc[:,['学号','总分']],how='left',on='学号')
print(result)

# 如果要保存一个单独的表，直接写  结果.to_excel(新路径)
# 如果想在原表上改：详见笔记19.3
# writer = pd.ExcelWriter(路径)
# 结果.to_excel(writer,index=False)
# writer.save()
# writer.close()

# 主要讲的是如果指定列的位置：
# 我用的方法是，先把需要调整的列的数据拿出来，之后，再将这个列删掉，最后，再用插入的方式把这个列调整到对应的位置上。
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件028-029/Vlookup.xlsx'
数据1 = pd.read_excel(路径,sheet_name='花名册')
数据2 = pd.read_excel(路径,sheet_name='成绩单')
结果 = pd.merge(数据1,数据2.loc[:,['学号','总分']],how='left',on='学号')
print(结果)
结果_总分 = 结果.总分
结果 = 结果.drop('总分',axis=1)   # 笔记10.1
结果.insert(0,'总分',结果_总分)    # Py基础篇PPT第30页在指定位置新增数据
print(结果)
writer = pd.ExcelWriter(路径)
结果.to_excel(writer,index=False)
writer.save()
writer.close()




























