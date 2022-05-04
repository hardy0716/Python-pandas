# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:56:58 2022

@author: 15517
"""
# 25.Pandas 中的行列转换
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/转换.xlsx'
data = pd.read_excel(path)
print(data)

data2 = pd.DataFrame(data.values.T,index=data.columns,columns=data.index)
print(data2)


# 26. Pandas中的环比
# 环比： (本期-上期)/上期
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/环比.xlsx'
data = pd.read_excel(path,'Sheet1')
# data['上月'] = data.金额.shift()
上月 = data.销售金额.shift()
环比 = (data.销售金额-上月)/上月
data['环比'] = 环比
print(data)

data = pd.read_excel(path,'Sheet2')
def 公式(ndata):
    ndata['环比'] = ndata.金额 - ndata.金额.shift()
    return ndata
data2 = data.sort_values(['城市','月份']).groupby('城市').apply(公式)
print(data2)




# 26.Pandas 中的同比
# 同比 = (本期-去年同期)/去年同期
import pandas as pd
path = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件030-031/同比.xlsx'
data = pd.read_excel(path,'Sheet1')
year = data['日期'].dt.year
data2 = pd.pivot_table(data,index='店号',values='金额',columns=year,aggfunc='sum')
同比 = (data2[2019]-data2[2018])/data2[2018]
data2['同比'] = 同比
print(data2)











