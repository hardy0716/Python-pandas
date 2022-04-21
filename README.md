# Python-pandas
孙兴华 py_pandas

# 数据类型与新建文件
数据类型	             说明	                        新建方法
csv、tsv、txt	  用逗号分隔、tab分割的纯文本文件 	   pd.to_csv
excel	                  xls或xlsx	                  pd.to_excel
mysql	               关系数据库表	                   pd.to_sql


# 新建文件同时写入数据并设置索引
import pandas as pd
路径 = 'c:/pandas/新建空白文件.xlsx'
数据=pd.DataFrame({'id':[1,2,3],'姓名':['叶问','李小龙','孙兴华']}) # 写入的数据
数据=数据.set_index('id')  # 将id设置为索引
数据.to_excel(路径)    # 将数据写入Excel文件
print(数据)

# 读取数据
数据类型	        说明	              读取方法
csv、tsv、txt   	默认逗号分隔	      pd.read_csv
csv、tsv、txt	    默认\t分隔	        pd.read_table
excel	            xls或xlsx	          pd.read_excel
mysql	            关系数据库表	        pd.read_sql

读取txt文件与csv文件
# pd.read_csv
# pd.read_table
体验两种方法的区别，与sep指定分隔符
# 切记：如果分隔符不止一种，使用正则表达式sep='\s+'
一、读取数据
import pandas as pd           
路径 = 'c:/pandas/读取文件.csv'     
读取数据 = pd.read_csv(路径)        
print(读取数据)        
二、查看前几行数据
print(读取数据.head())     # 默认是5行，指定行数写小括号里
三、查看数据的形状，返回（行数、列数）
print(读取数据.shape)
四、 查看列名列表
print(读取数据.columns)
五、查看索引列
print(读取数据.index)
六、查看每一列数据类型
print(读取数据.dtypes)

# 自己指定分隔符、列名
读取数据 = 读取数据 = pd.read_csv(路径,sep=',',header=None,names=['a','b','c'],encoding='utf-8',index_col='a')
英文逗号或"\t",从文件、url、文件型对象中加载带分隔符的数据，默认为'\t'。（read_csv默认分隔符是逗号）,可以通过制定sep 参数来修改默认分隔符
读取没有标题的文件时，默认为第一行作为列标题,设置header=None,意思就是没有表头，后面你自己写表头
# 注意：你的txt文档必需另存为utf-8编码，如果是ASCII报错!
sep 分隔符 或正则表达式 sep = '\s+'
header 列明的行号， 默认为0(第一行)，如果没有列名应该为None
names 列名，与header=None一起使用
index_col  索引的列名或列号，可以是一个单一的名称或数字，也可以是一个分层索引
skiprows  从文件开始处，需要跳过的行数或行号列表
encoding  文本编码，例如 utf-8
nrows  从文件开头处读入的行数  nrows = 3

# txt文件转csv文件
数据 = pd.read_csv('c:/pandas/读取文件.txt')
数据.to_csv('c:/pandas/读取文件.csv')

# 读取Mysql数据库
连接对象 = pymysql.connect(host = 'localhost',user = 'root',password = '1234',database = 'test',charset = 'utf8')
读取文件 = pd.read_sql("select * from 1班",con=连接对象)

# 读取Excel文件
路径 = 'c:/pandas/读取文件.xlsx'
读取数据 = pd.read_excel(路径,header=None,names=['序号','姓名','年龄','手机','地址','入职日期'],index_col='序号')
print(读取数据)
读取数据.to_excel(路径)

# pandas的数据结构
DataFrame：二维数据，整个表格，多行多列   【简称df】
df.index：索引列
df.columns：列名
Series：一维数据，一行或一列

# Series是一种类似于一维数组的对象，它由一组数据（不同数据类型）以及一组与之相关的数据标签（即索引）组成。

数据= pd.Series([520,'孙兴华',1314,'2020-07-30'])  # 左侧是索引，右侧是数据
数据= pd.Series([520,'孙兴华',1314,'2020-07-30'],index=['a','b','c','d'])  # 指定索引

字典={'姓名':'孙兴华','性别':'男','年龄':'20','地址':'花果山水帘洞'}
数据=pd.Series(字典)
print(数据)  # 查询整个字典
print(数据['姓名']) # 通过key可以查对应的值
type(数据['年龄'])  # 通过key可以查对应值的类型
print(数据[['姓名','年龄']])  # 通过多个key查对应的值
type(数据[['姓名','年龄']])   # 注意：他不返回值的类型，而返回Series

# Series只是一个序列，可能是一行，也可能是一列，现在无法确定用行的方法，把Series加入DataFrame，就是行，反之就是列。

# Series常用方法
数据.index #查看索引
数据.values #查看数值
数据.isnull() #查看为空的，返回布尔型
数据.notnull() 
数据.sort_index() #按索引排序
数据.sort_values() #按数值排序








