# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:39:26 2022

@author: 15517
"""

# 连接查询【数据合并与重塑】
# A inner join B 取A和B的交集
# A left join B  取A的所有（包含A、B的交集）  
# A right join B = B left join A

# 4.1 Merge
# 首先merge的操作非常类似sql里面的join，实现将两个Dataframe根据一些共有的列连接起来，当然，在实际场景中，这些共有列一般是Id，
# 连接方式也丰富多样，可以选择inner(默认)，left,right,outer 这几种模式，分别对应的是内连接，左连接，右连接，全外连接

# 参数
# how 数据融合的方法，存在不重合的键，方式（inner、outer、left、right）
# on  用来对齐的列名，一定要保证左表和右表存在相同的列名
# left_on 左表对齐的列，可以是列名，也可以是DataFrame同长度的arrays
# right_on 游标对齐的列，可以是列名
# left_index 将左表的index用作连接键
# right_index 将右表的index用作连接键
# suffixes  左右对象中存在重复列，结果区分的方式。后缀名
# copy  默认：True 将数据复制到数据结构中，设置为False提高性能

# 4.1.1 InnerMerge （内连接）
import numpy as np
import pandas as pd

data1= pd.DataFrame({'姓名':['叶问','李小龙','孙兴华','李小龙','叶问','叶问'],'出手次数1':np.arange(6)})
data2 = pd.DataFrame({'姓名':['黄飞鸿','孙兴华','李小龙'],'出手次数2':[1,2,3]})
data3 = pd.merge(data1,data2)
print(data3)

data3 = pd.merge(data1,data2,on='姓名',how='inner')
print(data3)

# 4.1.2 LeftMerge （左连接）
data4 = pd.merge(data1,data2,on='姓名',how='left')
print(data4)

# 4.1.3 RightMerge (右连接)
data5 = pd.merge(data1,data2,on='姓名',how='right')
print(data5)

# 4.1.4 OuterMerge (全连接)
data6 = pd.merge(data1,data2,on='姓名',how='outer')
print(data6)

# 4.1.5 MultipleKey Merge (基于多个key上的merge)
#　刚才我们都是仅仅实现的在一个key上的merge，当然我们也可以实现基于多个keys的merge

import pandas as pd
数据1 = pd.DataFrame({'姓名': ['张三', '张三', '王五'],'班级': ['1班', '2班', '1班'],'分数': [10,20,30]})
print(数据1)
数据2 = pd.DataFrame({'姓名': ['张三', '张三', '王五','王五'],'班级': ['1班', '1班', '1班','2班'],'分数': [40,50,60,70]})
print(数据2)
数据3= pd.merge(数据1,数据2,on=['姓名','班级'])     # 内连接（交集）的结果
print(数据3)
数据4= pd.merge(数据1,数据2,on=['姓名','班级'],how='outer')   # 外连接（并集）的结果
print(数据4)

数据5= pd.merge(数据1,数据2,on='姓名')
print(数据５)

数据6= pd.merge(数据1,数据2,on='姓名',suffixes=('_数据1','_数据2'))
print(数据６)


# 4.1.6 Merge on Index (基于index上的merge)
import pandas as pd
数据1 = pd.DataFrame({'姓名': ['张三','李四','王五','张三','李四'],'次数':range(5)})
数据2 = pd.DataFrame({'数据': [10, 20]}, index=['张三','李四'])
数据3=pd.merge(数据1,数据2,left_on='姓名',right_index=True)
# 用左表的left_on = '姓名' 连接 右表的索引 right_index = True,  默认内连接
print(数据3)

数据4=pd.merge(数据1,数据2,left_on='姓名',right_index=True,how='outer')
print(数据4)


# 4.1.7 总结
# 1.通过on指定数据合并对齐的列
# result = pd.merge(left, right, on=['key1', 'key2'])

# 2.没有指定how的话默认使用inner方法，除了内连接，还包括左连接、右连接、全外连接
# 左连接：
# result = pd.merge(left, right, how='left', on=['key1', 'key2'])

# 右连接：
# result = pd.merge(left, right, how='right', on=['key1', 'key2'])

# 全外连接：
# result = pd.merge(left, right, how='outer', on=['key1', 'key2'])

# 3.suffix后缀参数
# 如果表合并的过程中遇到有一列两个表都同名，但是值不同，合并的时候又都想保留下来，就可以用suffixes给每个表的重复列名增加后缀。
# result = pd.merge(left, right, on='k', suffixes=['_l', '_r'])






