# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:50:08 2022

@author: 15517
"""

# 1、导入pandas并查看版本
import numpy as np # optional
import pandas as pd
print(pd.__version__)  #1.3.4
print(pd.show_versions(as_json=True))


# 2、从列表list、numpy 数组array和 字典dict 中创建series
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
# Solution
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser3.head())


# 3、将系列的索引转换为数据框的一列
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
# Solution
df = ser.to_frame().reset_index()
print(df.head())

# 4、将多个Series组合成一个DataFrame
# Input
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

# Solution 1
df = pd.concat([ser1, ser2], axis=1)

# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head())

# 5、给系列索引命名
# Input
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

# Solution
ser.name = 'alphabets'
ser.head()

# 6、从ser1删除存在ser2中的项目
# Input
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
ser1[~ser1.isin(ser2)]

# 7、获取ser1和ser2不共同所有项目
# Input
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Solution
ser_u = pd.Series(np.union1d(ser1, ser2))  # union
ser_i = pd.Series(np.intersect1d(ser1, ser2))  # intersect
ser_u[~ser_u.isin(ser_i)]

# 8、获得数值系列的最小值、25th 百分位数、中位数、75th 和最大值
# Input
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))

# Solution
np.percentile(ser, q=[0, 25, 50, 75, 100])


# 9、计算每个唯一值的频率计数ser
# Input
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

# Solution
ser.value_counts()

# 10、只保留前 2 个最常用的值并将其他所有值替换为“other"
# Input
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# Solution
print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
ser













