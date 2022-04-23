# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 18:16:56 2022

@author: 15517
"""

# 计算列
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件011/计算列.xlsx'
数据 = pd.read_excel(路径,index_col='序号')
print(数据)
数据['销售金额'] = 数据['单价']*数据['销售数量']
print(数据)

# 如果使csv文件则要保证是utf-8，无论是在文件上改，还是用参数改，总之要改

# 如果不想全部运算，而只想计算一部分行的时候，需要用到for循环

路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件011/计算列.csv'
数据 = pd.read_csv(路径,index_col='序号')
for i in range(1,3):   #只计算1和2
    数据['销售金额'].at[i] = 数据['单价'].at[i]*数据['销售数量'].at[i]
print(数据)
#数据.to_csv(路径)


# 6.1 pandas apply() 函数

# 理解 pandas 的函数，要对函数式编程有一定的概念和理解。
# 函数式编程，包括函数式编程思维，当然是一个很复杂的话题，但对今天介绍的 apply() 函数，
# 只需要理解：函数作为一个对象，能作为参数传递给其它参数，并且能作为函数的返回值。


# pandas 的 apply() 函数可以作用于 Series 或者整个 DataFrame，
# 功能也是自动遍历整个 Series 或者 DataFrame, 对每一个元素运行指定的函数

import pandas as pd
def 涨价(x):
    return x+3

路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件011/计算列.xlsx'
数据 = pd.read_excel(路径,index_col='序号')

数据['单价'] = 数据['单价'].apply(涨价)
print(数据)

# 或者使用 函数式编程 lambda 形参 : 表达式
数据['单价'] = 数据['单价'].apply(lambda x : x+3)
print(数据)

#　Series.apply()：民族为少数民族的加5分
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件011/apply函数.xlsx'
数据 = pd.read_excel(路径,index_col='序号')
print(数据)
数据['加分'] = 数据['民族'].apply(lambda x: 5 if x != '汉' else 0) #如果不是汉族　加分＝５　否则＝０
数据['最终分数'] = 数据['总分'] + 数据['加分']
print(数据)

# apply() 函数当然也可执行 python 内置的函数，
# 比如我们想得到 Name 这一列字符的个数，如果用 apply() 的话：
数据['姓名字符个数']=数据['姓名'].apply(len)
print(数据['姓名字符个数'])

#DataFrame.apply() 函数则会遍历每一个元素，对元素运行指定的 function。
#比如下面的示例：计算数组的平方
import numpy as np
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
数据=pd.DataFrame(arr,columns=['x','y','z'],index=['a','b','c']).

数据=pd.DataFrame(arr,columns=list('xyz'),index=list('abc')) #见Python基础篇 PPT笔记P42页
print(数据.apply(np.square))


# 如果只想 apply() 作用于指定的行和列，可以用行或者列的 name 属性进行限定。
# 比如下面的示例将 x 列进行平方运算：
数据2 = 数据.apply(lambda  a : np.square(a) if a.name=='x' else a)  #这里a.name 是会遍历每一个值 此a非彼a
print(数据2)

# 对 x 和 y 列进行平方运算：  
数据3 = 数据.apply(lambda  a : np.square(a) if a.name in ['x','y'] else a)
print(数据3)


# 第一行 （a 标签所在行）进行平方运算：
数据4 = 数据.apply(lambda m : np.square(m) if m.name == 'a' else m, axis=1)
print(数据4)

# 第一行和第三行（a标签和c标签所在行）进行平方运算：
数据4 = 数据.apply(lambda m : np.square(m) if m.name in ['a','c'] else m, axis=1)
print(数据4)

# 默认情况下 axis=0 表示按列，axis=1 表示按行。


# 6.2 apply函数计算日期相减
# 平时我们会经常用到日期的计算，比如要计算两个日期的间隔，
# 比如下面的一组关于起止日期的数据：

路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件011/计算日期.xlsx'
数据 = pd.read_excel(路径,index_col='序号')
print(数据)
数据['间隔'] = 数据['结束日期'] - 数据['起始日期']  # 结果带有days

间隔1 = 数据['结束日期'] - 数据['起始日期']
数据['间隔1'] = 间隔1.apply(lambda x : x.days)  # 结果无days

print(数据)







