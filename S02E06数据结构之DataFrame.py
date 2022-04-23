# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:19:04 2022

@author: 15517
"""

# DataFrame是一个表格型的数据结构
# 	• 每列可以是不同的值类型（数值、字符串、布尔值等）
# 	• 既有行索引index，也有列索引columns
# 	• 可以被看做由Series组成的字典
# 创建DataFrame最常用的方法，参考读取CSV、TXT、Excel、MySQL等
import pandas as pd
data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(data)
print(data['a'][0])
print(data.loc[0]['b'])
print(data.iloc[0][1])
print(data[['a','b']])

# loc根据index来索引对应的行。
# iloc并不是根据index来索引，而是根据行号进行索引，行号从0开始，逐次加1

    #a： 数据.loc方法 根据行、列的标签值进行查询
    #b:  数据.iloc方法 根据行、列的数字位置查询

# 3.2.1 DataFrame 整个表格

# 多个字典序列创建DataFrame
import pandas as pd
dict = {
        'name':['孙兴华','李小龙','叶问'],
        'age':[20,80,127],
        'Gongfu':['撸铁','截拳道','咏春']
        }
data1 = pd.DataFrame(dict)
print(data1)
print(data1.dtypes)  #返回每一列的类型
print(data1.columns) #返回列索引，以列表形式返回：[列名1,列名2..]
print(data1.index)   #返回行索引， (start,stop,step)

# 从DataFrame 中查询Series

#如果只查询一列，返回的是pd.Series
print(data1['name']) #返回索引和这一列数据
type(data1['name'])  #类型返回Series  pandas.core.series.Series

#如果只查询一行，返回的是pd.Series
print(data1.loc[1])  #这时，它的索引为列名
type(data1.loc[1])   #类型返回Series  pandas.core.series.Series
 
#如果查询多列，返回的时pd.DataFrame
print(data1[['name','age']])  #返回索引和这两列的数据
type(data1[['name','age']])   #类型返回DataFrame pandas.core.series.DataFrame

#如果查询多行,返回的时pd.DataFrame
print(data1.loc[0:2])  #返回前三行，包括结束值0、1、2
type(data1.loc[0:2])   #类型返回DataFrame pandas.core.series.DataFrame


#3.2.3 将多个Series加入DataFrame
import pandas as pd
data1 = pd.Series(['叶问','李小龙','孙兴华'],index=[1,2,3],name='name')
data2 = pd.Series(['男','男','男'],index=[1,2,3],name='sex')
data3 = pd.Series([127,80,20],index=[2,3,4],name='age')
df1 = pd.DataFrame({data1.name:data1,data2.name:data2,data3.name:data3})
print(df1)

df2 = pd.DataFrame([data1,data2,data3])
print(df2)

# 注： 3个数据的index有对齐的功能，例如把data3的index改为2，3，4，没有值的地方会显示nan


# DataFrame 常用方法
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件006/数据结构 - 副本.xlsx'
数据 = pd.read_excel(路径,header=None,names=['序号','姓名','年龄','手机','地址','入职日期'],index_col='序号')

数据.head( 5 ) #查看前5行
数据.tail( 3 ) #查看后3行
数据.values #查看数值
数据shape #查看行数、列数
数据.fillna(0) #将空值填充0
数据.replace( 1, -1) #将1替换成-1
数据.isnull() #查找数据中出现的空值
数据.notnull() #非空值
数据.dropna() #删除空值
数据.unique() #查看唯一值
数据.reset_index() #修改、删除，原有索引，详见例1
数据.columns #查看数据的列名
数据.index #查看索引
数据.sort_index() #索引排序 
数据.sort_values('入职日期') #值排序
pd.merge(数据1,数据1) #合并
pd.concat([数据1,数据2]) #合并，与merge的区别，自查
pd.pivot_table( 数据 ) #用df做数据透视表（类似于Excel的数透）


# 例1
print(数据.reset_index(drop=True))  #索引被直接删除
print(数据.reset_index(drop=False)) #索引列会被还原为普通列















