# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:44:40 2022

@author: 15517
"""

# 一、读取文件
import pandas as pd
路径 =  'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件001-005/读取文件.xlsx'
读取数据 = pd.read_excel(路径)
读取数据 = pd.read_excel(路径,header=None,names=['序号','姓名','年龄','电话','地址','入职日期'],index_col='序号')
# 读取数据.columns = ['序号','姓名','年龄','电话','地址','入职日期'] #给每个列重复设置表头
# 读取数据 = 读取数据.set_index('序号',inplace=True)                #只在index上面改，不要生成新的
print(读取数据.columns)
print(读取数据)
读取数据.to_excel(路径)                                         #写入excel文件

#二、查看前几行数据
print(读取数据.head())    # 默认是5行，指定行数写小括号里
#三、查看数据的形状，返回（行数、列数）
print(读取数据.shape)
# 四、 查看列名列表
print(读取数据.columns)
#五、查看索引列
print(读取数据.index)
#六、查看每一列数据类型
print(读取数据.dtypes)














