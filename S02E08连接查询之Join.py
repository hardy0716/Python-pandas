# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 08:48:09 2022

@author: 15517
"""

# 4.2 Join

import pandas as pd
left_dict = {'name1':['叶问','李小龙','孙兴华'],'age1':[127,80,20]}
right_dict={'name2':['大刀王五','霍元甲','陈真'],'age2':[176,152,128]}
left = pd.DataFrame(left_dict)
right = pd.DataFrame(right_dict)
print(left.join(right))
# join无非就是合并，默认是横向，还有一个点需要注意的是，
# 我们其实可以通过join实现和merge一样的效果   merge可能更好一些

# join将两个DataFrame中不同的列索引合并成为一个DataFrame
# 参数的意义与merge基本相同，只是join方法 默认左外连接 how=left

# def join(self, other, on=None, how='left', lsuffix='', rsuffix='',sort=False):

# （1）on参数
# result = left.join(right, on='key')

# （3）组合多个dataframe
# 一次组合多个dataframe的时候可以传入元素为dataframe的列表或者tuple。
# 一次join多个，一次解决多次烦恼~

#  right2 = pd.DataFrame({'v': [7, 8, 9]}, index=['K1', 'K1', 'K2'])
# result = left.join([right, right2])




















