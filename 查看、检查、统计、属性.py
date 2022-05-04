# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:20:50 2022

@author: 15517
"""

df.head(n) # 查看 DataFrame 对象的前n行
df.tail(n) # 查看 DataFrame 对象的最后n行
df.sample(n) # 查看 n 个样本，随机
df.shape # 查看行数和列数
df.info() # 查看索引、数据类型和内存信息
df.describe() # 查看数值型列的汇总统计
df.dtypes # 查看各字段类型
df.axes # 显示数据行和列名
df.mean() # 返回所有列的均值
df.mean(1) # 返回所有行的均值，下同
df.corr() # 返回列与列之间的相关系数
df.count() # 返回每一列中的非空值的个数
df.max() # 返回每一列的最大值
df.min() # 返回每一列的最小值
df.median() # 返回每一列的中位数
df.std() # 返回每一列的标准差
df.var() # 方差
s.mode() # 众数
s.prod() # 连乘
s.cumprod() # 累积连乘,累乘
df.cumsum(axis=0) # 累积连加,累加
s.nunique() # 去重数量，不同值的量
df.idxmax() # 每列最大的值的索引名
df.idxmin() # 最小
df.columns # 显示所有列名
df.team.unique() # 显示列中的不重复值
# 查看 Series 对象的唯一值和计数, 计数占比: normalize=True
s.value_counts(dropna=False)
# 查看 DataFrame 对象中每一列的唯一值和计数
df.apply(pd.Series.value_counts)
df.duplicated() # 重复行
df.drop_duplicates() # 删除重复行
# set_option、reset_option、describe_option 设置显示要求
pd.get_option()
# 设置行列最大显示数量，None 为不限制
pd.options.display.max_rows = None
pd.options.display.max_columns = None
df.col.argmin() # 最大值[最小值 .argmax()] 所在位置的自动索引
df.col.idxmin() # 最大值[最小值 .idxmax()] 所在位置的定义索引
# 累计统计
ds.cumsum() # 前边所有值之和
ds.cumprod() # 前边所有值之积
ds.cummax() # 前边所有值的最大值
ds.cummin() # 前边所有值的最小值
# 窗口计算(滚动计算)
ds.rolling(x).sum() #依次计算相邻x个元素的和
ds.rolling(x).mean() #依次计算相邻x个元素的算术平均
ds.rolling(x).var() #依次计算相邻x个元素的方差
ds.rolling(x).std() #依次计算相邻x个元素的标准差
ds.rolling(x).min() #依次计算相邻x个元素的最小值
ds.rolling(x).max() #依次计算相邻x个元素的最大值