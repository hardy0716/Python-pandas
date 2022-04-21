# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:33:48 2022

@author: 15517
"""

# 一、读取数据
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件001-005/读取文件.txt'
读取数据 = pd.read_csv(路径)   # csv是以 逗号 进行分割的
# 读取数据 = pd.read_table(路径,sep = ',')  若使用table 默认为空格，需要指定分隔符
# 学习一下正则表达式
print(读取数据)

# 二、查看前几行数据
print(读取数据.head())   # 默认是5行，指定行数写在小括号里

# 三、查看数据的形状，返回（行数、列数）
print(读取数据.shape)
#四、查看列名列表
print(读取数据.columns)   #默认第一行是表头

#五、查看索引列
print(读取数据.index)

# 六、查看每一列数据类型
print(读取数据.dtypes)

# 2.1.2 自己制订分隔符、列名
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件001-005/读取文件.txt'
读取数据 = pd.read_csv(路径,sep = ',',header=None,names=['性别','姓名','年龄','电话','地址','入职日期'],encoding='utf-8',index_col='入职日期',skiprows=([2,3]))
# sep 英文逗号或"\t",从文件、url、文件型对象中加载带分隔符的数据，默认为'\t'
# (read_csv默认分隔符是逗号）,可以通过制定sep 参数来修改默认分隔符

#  读取没有标题的文件时，默认为第一行作为列标题,设置header=None,意思就是没有表头，后面你自己写表头
#  names 列名，与header=None一起使用
# 注意：你的txt文档必需另存为utf-8编码，如果是ASCII报错
# inderx_col 索引的列名或列名，可以是一个单一的名称或数字，也可以是一个分层索引
# skiprows 从文件开始处，需要跳过的行数或列号列表  skiprows = ([2,3])
# norws 从文件开头处读入的行数  nrows = 3

print(读取数据)



# 2.1.3 txt文件转csv文件
数据 = pd.read_csv('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件001-005/读取文件.txt')
数据.to_csv('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件001-005/读取文件.csv')
读取数据.to_csv('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件001-005/读取文件.csv')
print(数据)














