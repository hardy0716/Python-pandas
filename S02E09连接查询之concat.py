# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 09:10:37 2022

@author: 15517
"""

# Concat
import numpy as np
arr = np.arange(9).reshape((3,3))
print(arr)
arr1 = np.concatenate([arr,arr],axis=1)  #沿着1轴 二维（行0，列1）
print(arr1)
arr2 = np.concatenate([arr,arr],axis=0)  #沿着0轴 二维（行0，列1）
print(arr2)


# concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
#    keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)

# objs  合并的对象集合，可以是Series、DataFrame
# axis  合并的方法，默认为0，表示纵向，1为横向
# join  默认outer并集，inner交集，只有这两种方法
# join_axes  按哪些对象的索引保存
# ignore_index  默认False忽略。 是否忽略原index
# keys  为原始DataFrame添加一个键，默认无

# 4.3.1 在pandas中使用Concat
import pandas as pd      
data1 = pd.Series([0,1,2],index=['A','B','C'])
data2 = pd.Series([3,4],index=['D','E'])
data3 = pd.concat([data1,data2])
print(data3)

# 在上面的例子中，我们分别创建了两个没有重复Index的Series,
# 然后用concat默认的把它们合并在一起，这时生成的依然是Series类型

# 如果我们把axis换成1，那生成的就是Dataframe,像下面一样

data4 = pd.concat([data1,data2],axis=1,sort=True)
# sort=Ture是默认的，pandas总是默认index排序，默认axis=0
print(data4)


# 4.3.2 首尾相接
# 相同字段的表的首尾相接
dict1 = {'A':['A0','A1','A2'],'B':['B0','B1','B2']}
df1 = pd.DataFrame(dict1,index=[0,1,2])
dict2 = {'A':['A3','A4','A5'],'B':['B3','B4','B5']}
df2 = pd.DataFrame(dict2,index=[3,4,5])
dict3 = {'A':['A6','A7','A8'],'B':['B6','B7','B8']}
df3 = pd.DataFrame(dict3,index=[6,7,8])
frames = [df1,df2,df3]
result = pd.concat(frames)
print(result)

# 要在相接的时候再加上一个层次的key来识别数据源来自哪张表，可以增加key
result = pd.concat(frames,keys=['df1','df2','df3'])
print(result)


# 4.3.3 横向表拼接 （行对齐）

# 1.axis
#当axis = 1的时候，concat就是行对齐，然后将不同列名称的两张表合并

dict4 = {'B':['B2','B3','B6'],'D':['D2','D3','D6'],'F':['F2','F3','F6']}
df4 = pd.DataFrame(dict4,index=[2,3,6])
result = pd.concat([df1, df4], axis=1)
print(result)

# 2.join
# 加上join参数的属性，如果为inner得到的是两表的交集，如果是
# outer 得到的是两表的并集

result = pd.concat([df1,df4],axis=1,join='inner')
print(result)  # 上面result的完整行

result = pd.concat([df1,df4],axis=1,join='outer')
print(result)  # join默认为outer

# 3.join_axes   #目前的新版本已经取消了join_axes  可以换成merge
# 如果有join_axes的参数传入，可以指定根据哪个轴来对齐数据
# 如根据df1表对齐数据，就会保留指定的df1表的轴，然后将df4的表与之拼接
result = pd.concat([df1,df4],axis=1,join_axes=0)

result = pd.merge(df1,df4,how='left',left_index=True,right_index=True)
print(result)

help(pd.concat)
# ??????????????????

# 4.3.4 append
# append是Series和DataFrame的方法，使用它是默认沿着列进行凭借(axis=0,列对齐)

result = df1.append(df2)
print(result)


# 4.3.5 无视index的concat
# 如果两个表的index无实际含义，使用ignore_index参数，
# 合并两个表就是根据列字段对齐，然后合并。最后重新整理一个新的index

result = pd.concat([df1,df4],axis=0,ignore_index=True)
print(result)


# 4.3.6 合并的同时增加区分数据组的键
# 前面提到的keys参数可以用来给合并后的表增加key来区分不同的表数据来源

# 1.可以直接用key参数实现
result = pd.concat(frames,keys=['x','y','z'])
print(result)

# 2.传入字典来增加分组键
pieces = {'x':df1,'y':df2,'z':df3}
result = pd.concat(pieces)
print(result)


# 4.3.7 在DataFrame中加入新的行
# append 方法可以将Series和字典的数据作为DataFrame的新一行插入
s2 = pd.Series(['X0','X1'],index=['A','B'])
result = df1.append(s2,ignore_index=True)
print(result)

# 4.3.8 表格列字段不同的表合并
# 如果遇到两张表的列字段本来就不一样，但又想合并两个表
# 其中无效的值用nan表示。可以用ignore_index来实现
dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4}, {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]
result = df1.append(dicts, ignore_index=True)
print(result)

##########总结
# concat : 可以沿着一条轴将多个对象连接到一起
# merge  ：可以根据一个或多个键将不同的DataFrame中的行连接起来
# join   : inner是交集，outer是并集







