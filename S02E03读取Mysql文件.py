# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:21:56 2022

@author: 15517
"""

import pandas as pd
# pip install pymysql
import pymysql
# 参数： host 主机名； 用户名 user； 密码 password； 数据库名 database
连接对象 = pymysql.connect(host = 'localhost',user = 'root',password = '123456',database = 'monkey',charset = 'utf8')
读取文件 = pd.read_sql("select * from course",con=连接对象) 
#读取文件 = pd.read_sql("select * from course",con=连接对象,index_col=['courseid','coursename']) 
# 第1个参数是SQL查询语句，第2参数是数据库连接
print(读取文件)





























