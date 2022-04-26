# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:11:54 2022

@author: 15517
"""

#　筛选
# 一、加载数据
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件013-014/筛选.xlsx'
data = pd.read_excel(path,index_col='序号',sheet_name='Sheet1')
print(data)

# 二、按位置筛选，筛选第2行至第4行数据
data = pd.read_excel(path,index_col='序号',sheet_name='Sheet1')
data1 = data.loc[2:4]   # 按照序号抽取 2，3，4
print(data1)

#　三、按值过滤，筛选所有男性
cond1 = data['性别'] == '男'  # 判断语句 布尔值
print(cond1)
print(data[cond1])

# 四、多条件筛选，男性 和 总分大于等于150
cond2 = data[cond1]['总分'] > 150
print(data[cond1][cond2])


cond2 = "性别 == '男' and 总分 >= 150"
print(data.query(cond2))

# query方法，可以直接接受一个查询字符串
cond3 = "姓名 in ['王松','王刚']"
print(data.query(cond3))


# 9.1 文本筛选： 开头和结尾

# startwith()  endwith()
# startswith()  判断字符串是否以指定字符或子字符串开头。
# 语法： str.endwith("suffix",start,end) 或
# str[start,end].endswith("suffix")用于判断字符串中某段字符串是否以指定字符或子字符串结尾
# suffix — 后缀，可以是单个字符，也可以是字符串，还可以是元组（"suffix"中的引号要省略）
# start 索引字符串的起始位置； end 结束位置
# str.endwith(suffix) start 默认为0,end默认为字符串的长度减1 （len(str)-1）

# 例如： 姓名开头姓王的
cond4 = data['姓名'].str.startswith('王') # 如果是结尾改为endwith
print(data[cond4])      #??????????




# 9.2 文本筛选： 包含

# str.contains(par,case=True,flags=0,na=nan,regex=True) 是否包含查找的字符串

# pat: 字符串/正则表达式
# case: 布尔值，默认为True,如果为True则匹配敏感
# flags: 整型，默认为0（没有flags）
# na： 默认为Nan，替换缺失值
# regex： 布尔值，默认为True,如果为真则使用re.research，否则使用python
# 返回值为 布尔值的序列或数组

# 例1：筛选地址包含信阳市
cond5 = data['地址'].str.contains('信阳市')
print(data[cond5])

cond6 = data['地址'].str.contains('[a-cA-C]座')
print(data[cond6])

# 9.3筛选值范围
# 语文分数在60至100分之间的女性
cond = "60 <= 语文 <= 100 and 性别 == '女'"
print(data.query(cond))


# 9.4筛选日期
# 9.4.1 获取某年某月数据

data = pd.read_excel(path,index_col='出生日期',parse_dates=['出生日期'])
# parse_dates=['出生日期'] 将出生日期列转为日期格式
print(data)

print(data['1983'].head())
print(data['1983-10'].head())

# 9.4.2 获取某个时期之前或之后的数据
data1 = data.sort_values('出生日期')

# truncate() 函数
# 获取某个日期之前/后或时间区间的数据
# dataframe的.truncate()函数可以截取某个时期之前或之后的数据，或者某个时间区间的数据，进行统计分析。
# DataFrame.truncate(before=None, after=None, axis=None, copy=True)

# before：取值范围：date，string，int，是指截断此索引值之前的所有行
# after：取值范围：date，string，int，是指截断此索引值后的所有行
# axis：取值范围：{0或’index’，1或’columns’}（可选），是指轴截断。 默认情况截断索引（行）。
# copy：取值范围：boolean，默认为True，返回截断部分的副本



# 获取1980年以后的数据  before
print(data1.truncate(before='1980').head(10))

# 获取1990-12之前的数据  after
print(data1.truncate(after='1990-12').head(10))

# 获取1990-02年以后的数据
print(data1.truncate(before='1990-02').head())

# 获取1984-01-01年以后的数据
print(data1.truncate(before='1984-01-01').head())

# 获取指定时间区间
print(data1['1983':'1990'])
print(data1['1983-01-1':'1990-12-31'])


# 9.4.3 【推荐】多条件日期范围
import pandas as pd
import datetime as dt
data = pd.read_excel(path,index_col='序号',parse_dates=['出生日期'])

cond = (
        '@data.出生日期.dt.year > 1980 and'
        '@data.出生日期.dt.year < 1990'
        'and 性别 == "男"'
)
print(data.query(cond))










