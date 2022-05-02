# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:13:12 2022

@author: 15517
"""

# 19.1 一个文件夹下多个工作簿的合并【单独Sheet】
# 1、把文件夹下面所有的文件都遍历出来
# 2、循环读取每个文件
    #(1)第一次读取的文件放入一个空表中，起名叫合并表
    #(2)从第二次开始每次都与这个合并表进行合并
# 3、写入Excel
# 4、所有表的表头行数要一致，通过header=1进行设置

import pandas as pd
import os
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025/'
合并表 = pd.DataFrame()
for 文件名 in os.listdir(路径):
    表格 = pd.read_excel(路径 + 文件名)
    合并表 =pd.concat([合并表,表格])
print(合并表)


import pandas as pd
import os
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-2/'
合并表 = pd.DataFrame()
for 文件名 in os.listdir(路径):
    表格 = pd.read_excel(路径 + 文件名,header=1)
    合并表 =pd.concat([合并表,表格])
合并表 = 合并表.set_index('日期') # 重新设置索引
print(合并表)

# 保存：
路径2 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-2/合并表.xlsx'
合并表.to_excel(路径2)


# 19.2 同一工作簿中多个Sheet合并
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-3/合并2.xlsx'
数据 = pd.read_excel(路径,None,index_col='序号')
合并表 = pd.DataFrame()
字段名 = list(数据.keys()) # 返回['序号', '姓名', '电话']
for 列标签 in 字段名:
    新数据 = 数据[列标签]
    合并表 = pd.concat([合并表,新数据])
print(数据)
路径2 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-3/合并表.xlsx'
合并表.to_excel(路径2)

# 19.3 ExcelWriter针对不同工作表的操作
# 使用ExcelWriter()可以向同一个excel的不同sheet中写入对应的表格数据，
# 首先需要创建一个writer对象，传入的主要参数为已存在容器表格的路径及文件名称:

# ExcelWriter对已经设置好的格式是无法更改的，因此，由pandas转成excel的时候，
# 必须将格式清除，尤其是表头的格式，代码如下：
import pandas.io.formats.excel
pandas.io.formats.excel.header_style = None

# 标准的保存pandas表到excel的形式为
# writer = pd.ExcelWriter(‘c:/123.xlsx’)
# 数据.to_excel(writer, '工作表名')  # 这里假设数据是一个pandas的dataframe
# writer.save()
# writer.close()


# 19.4 将一个工作表拆成多个工作表
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-3/拆分.xlsx'
数据 = pd.read_excel(路径)
分割列 = list(数据['部门'].drop_duplicates()) # 返回：['办公室', '销售部', '保洁部']，笔记13.1
新数据 = pd.ExcelWriter('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-3/多个Sheet.xlsx')
for i in 分割列:
    数据1 = 数据[数据['部门'] == i]
    数据1.to_excel(新数据,sheet_name=i)
新数据.save()
新数据.close()

# 19.5 将一个工作簿拆分成多个工作簿
import pandas as pd
路径 = 'D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-3/拆分.xlsx'
数据 = pd.read_excel(路径)
分割列 = list(数据['部门'].drop_duplicates()) # 返回：['办公室', '销售部', '保洁部']
for i in 分割列:
    数据1 = 数据[数据['部门'] == i]
    数据1.to_excel('D:/softwares/Python/python_work/SXH/SXH_Pandas/pandas教程/课件025/课件025-3/'+ i + '.xlsx')



























