# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:31:22 2022

@author: 15517
"""

# 填充常用类型数据
# 1. pd.read_excel参数：
# skiprows = 行数  跳过几行
# usecols = '区域' 和Excel中一样，就是一个列的区域
# index_col = '字段名' 将谁设置为索引
# dtype = {'序号':str,'性别':str,'日期':str}   # 防止出错，把类型全指定为字符型

# 2. 数据.at的用法
# 作用：获取某个位置的值，例如，获取第0行，第a列的值，即：index=0，columns='a'
# 变量名 = 数据.at[0, 'a']

# 3.日期模块 datetime

import pandas as pd
import datetime as dt # 日期模块
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件010/自动填充.xlsx'
起始日期 = dt.date(2022, 4, 23)
读取数据 = pd.read_excel(路径,skiprows=8,usecols="F:I",index_col=None,dtype={'序号':str,'性别':str,'日期':str})
# 都改为str字符型 防止报错
print(读取数据)
for i in 读取数据.index:
    读取数据['序号'].at[i] = i + 1    #已经把'序号'切出来了
    读取数据['性别'].at[i] = '男' if i%2 == 0 else '女'  #偶数为男
    #读取数据['日期'].at[i] = 起始日期 + dt.timedelta(days=i) #timedelta 只能加天，小时，秒，毫秒
    读取数据['日期'].at[i]=dt.date(起始日期.year+i, 起始日期.month, 起始日期.day) #如果要在年上累加用date
print(读取数据)
 

   
#但是月的累计很麻烦，因为累加到12月就要进1位到年份上
import pandas as pd
import datetime as 日期模块
def 累加月(d,md):    # （日期，传递的月份）
    yd = md // 12   # yd年  md // 12 地板除 # 如 3//2 = 1
    m = d.month + md % 12  # 日期的月份 加上 传递月份除以12的余数
    if m != 12:
        yd += m // 12  
        m = m % 12
    return 日期模块.date(d.year + yd,m,d.day)


路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件010/自动填充.xlsx'
起始日期 = 日期模块.date(2022,4,23)
读取数据 = pd.read_excel(路径,skiprows=8,usecols="F:I",index_col=None,dtype={'序号':str,'性别':str,'日期':str})
for i in 读取数据.index:
    读取数据['序号'].at[i] = i+1
    读取数据['性别'].at[i] = '男' if i%2 == 0 else '女'
    读取数据['日期'].at[i] = 累加月(起始日期,i)
读取数据.set_index('序号',inplace=True)    # 只在index上面改,不要生成新的
print(读取数据)
读取数据.to_excel(路径)



#以上的方法是先拿到Series再改值，下面的方法是在DataFrame上直接改值
import pandas as pd
import datetime as 日期模块
def 累加月(d,md):
    yd = md // 12
    m =d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return 日期模块.date(d.year + yd,m,d.day)

路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件010/自动填充.CSV'
起始日期 = 日期模块.date(2022,4,23)
读取数据 = pd.read_excel(路径,skiprows=8,usecols="F:I",index_col=None,dtype={'序号':str,'性别':str,'日期':str})


for i in 读取数据.index:
    读取数据.at[i,'序号'] = i + 1
    读取数据.at[i,'性别'] = '男' if i % 2 == 0 else '女'
    读取数据.at[i,'日期'] = 累加月(起始日期,i)
读取数据.set_index('序号',inplace=True)
print(读取数据)
读取数据.to_csv(路径)











