# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:52:47 2022

@author: 15517
"""

to_excel方法定义：
DataFrame.to_excel(路径, sheet_name='Sheet1', na_rep='',
 float_format=None, columns=None, header=True, index=True, 
 index_label=None, startrow=0, startcol=0, engine=None, 
 merge_cells=True, encoding=None, inf_rep='inf', verbose=True, 
 freeze_panes=None)
（1）路径: 字符串或ExcelWriter 对象，文件路径或现有的ExcelWriter
（2）sheet_name :字符串,默认“Sheet1”，将包含DataFrame的表的名称。
（3）na_rep : 字符串,默认‘ ’缺失数据表示方式
（4）float_format : 字符串,默认None，格式化浮点数的字符串
（5）columns : 序列,可选，要编写的列
（6）header : 布尔或字符串列表，默认为Ture。写出列名。如果给定字符串列表，则假定它是列名称的别名。
（7）index :布尔,默认的Ture  写行名（索引）
（8）index_label : 字符串或序列，默认为None。如果需要，可以使用索引列的列标签。如果没有给出，标题和索引为true，则使用索引名称。如果数据文件使用多索引，则需使用序列。
（9）startrow :左上角的单元格行来转储数据框
（10）startcol :左上角的单元格列转储数据帧
（11）engine : 字符串,默认没有 使用写引擎 - 您也可以通过选项io.excel.xlsx.writer，io.excel.xls.writer和io.excel.xlsm.writer进行设置。
（12）merge_cells : 布尔,默认为Ture  编码生成的excel文件。 只有xlwt需要，其他编写者本地支持unicode。
（13）inf_rep : 字符串,默认“正” 无穷大的表示(在Excel中不存在无穷大的本地表示)
（14）freeze_panes : 整数的元组(长度2)，默认为None。