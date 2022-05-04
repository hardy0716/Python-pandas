# Python-pandas

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

# DataFrame是一个表格型的数据结构
	• 每列可以是不同的值类型（数值、字符串、布尔值等）
	• 既有行索引index，也有列索引columns
可以被看做由Series组成的字典
创建DataFrame最常用的方法，参考读取CSV、TXT、Excel、MySQL等!

import pandas as pd
数据=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['a','b','c'])
print(数据)
print(数据['a'][0] )
print(数据.loc[0]['a'] )
print(数据.iloc[0][0] )
print(数据[['a','b']])

# loc就根据这个index来索引对应的行。iloc并不是根据index来索引，而是根据行号来索引，行号从0开始，逐次加1。
		a. 数据.loc方法：根据行，列的标签值查询
    b.数据.iloc方法：根据行，列的数字位置查询
    
# 常用方法
数据.head( 5 ) #查看前5行
数据.tail( 3 ) #查看后3行
数据.values #查看数值
数据shape #查看行数、列数
数据.fillna(0) #将空值填充0
数据.replace( 1, -1)  #将1替换成-1
数据.isnull() #查找数据中出现的空值
数据.notnull() #非空值
数据.dropna() #删除空值
数据.unique() #查看唯一值
数据.reset_index() #修改、删除，原有索引，详见例1
数据.columns #查看数据的列名
数据.index #查看索引
数据.sort_index() #索引排序 
数据.sort_values() #值排序
pd.merge(数据1,数据1) #合并
pd.concat([数据1,数据2]) #合并，与merge的区别，自查
pd.pivot_table( 数据 ) #用df做数据透视表（类似于Excel的数透）

import pandas as pd
路径 = 'c:/pandas/读取文件.xlsx'
读取数据 = pd.read_excel(路径,header=None,names=['序号','姓名','年龄','手机','地址','入职日期'],index_col='序号')
print(读取数据.reset_index(drop=True)) # 索引被直接删除
print(读取数据.reset_index(drop=False)) # 索引列会被还原为普通列 


# Merge
# 首先merge的操作非常类似sql里面的join，实现将两个Dataframe根据一些共有的列连接起来，当然，在实际场景中，这些共有列一般是Id，
# 连接方式也丰富多样，可以选择inner(默认)，left,right,outer 这几种模式，分别对应的是内连接，左连接，右连接，全外连接

# 参数
how 数据融合的方法，存在不重合的键，方式（inner、outer、left、right）
on  用来对齐的列名，一定要保证左表和右表存在相同的列名
left_on 左表对齐的列，可以是列名，也可以是DataFrame同长度的arrays
right_on 游标对齐的列，可以是列名
left_index 将左表的index用作连接键
right_index 将右表的index用作连接键
suffixes  左右对象中存在重复列，结果区分的方式。后缀名
copy  默认：True 将数据复制到数据结构中，设置为False提高性能

# inner 内连接
数据3 = pd.merge(数据1,数据2,on='姓名',how='inner')

# leftmerge 左连接
数据3 = pd.merge(数据1,数据2,on='姓名',how='left')

# rightmerge 右连接
数据3 = pd.merge(数据1,数据2,on='姓名',how='right')

# outermerge 全连接
数据3 = pd.merge(数据1,数据2,on='姓名',how='outer')

# MultipleKey Merge (基于多个key上的merge)
import pandas as pd
数据1 = pd.DataFrame({'姓名': ['张三', '张三', '王五'],'班级': ['1班', '2班', '1班'],'分数': [10,20,30]})
print(数据1)
数据2 = pd.DataFrame({'姓名': ['张三', '张三', '王五','王五'],'班级': ['1班', '1班', '1班','2班'],'分数': [40,50,60,70]})
print(数据2)
数据3= pd.merge(数据1,数据2,on=['姓名','班级'])     # 内连接（交集）的结果
print(数据3)
数据4= pd.merge(数据1,数据2,on=['姓名','班级'],how='outer')   # 外连接（并集）的结果
print(数据4)

# Merge on Index (基于index上的merge)
数据1 = pd.DataFrame({'姓名': ['张三','李四','王五','张三','李四'],'次数':range(5)})
数据2 = pd.DataFrame({'数据': [10, 20]}, index=['张三','李四'])
数据3=pd.merge(数据1,数据2,left_on='姓名',right_index=True)
print(数据3)

数据4=pd.merge(数据1,数据2,left_on='姓名',right_index=True,how='outer')

# 总结
（1）通过on指定数据合并对齐的列
result = pd.merge(left, right, on=['key1', 'key2'])

2）没有指定how的话默认使用inner方法，除了内连接，还包括左连接、右连接、全外连接
左连接：
result = pd.merge(left, right, how='left', on=['key1', 'key2'])

右连接：
result = pd.merge(left, right, how='right', on=['key1', 'key2'])

全外连接：
result = pd.merge(left, right, how='outer', on=['key1', 'key2'])

（2）suffix后缀参数
如果表合并的过程中遇到有一列两个表都同名，但是值不同，合并的时候又都想保留下来，就可以用suffixes给每个表的重复列名增加后缀。
result = pd.merge(left, right, on='k', suffixes=['_l', '_r'])

# Join 
join无非就是合并，默认是横向，还有一个点需要注意的是，我们其实可以通过join实现和merge一样的效果
# join方法将两个DataFrame中不同的列索引合并成为一个DataFrame参数的意义与merge基本相同，只是join方法默认左外连接how=left
def join(self, other, on=None, how='left', lsuffix='', rsuffix='',sort=False):

（1）on参数
result = left.join(right, on='key')

（3）组合多个dataframe
一次组合多个dataframe的时候可以传入元素为dataframe的列表或者tuple。一次join多个，一次解决多次烦恼~
right2 = pd.DataFrame({'v': [7, 8, 9]}, index=['K1', 'K1', 'K2'])
result = left.join([right, right2])


# concat 
# concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)

objs  合并的对象集合，可以是Series、DataFrame
axis  合并的方法，默认为0，表示纵向，1为横向
join  默认outer并集，inner交集，只有这两种方法
join_axes  按哪些对象的索引保存
ignore_index  默认False忽略。 是否忽略原index
keys  为原始DataFrame添加一个键，默认无

# 4.3.1 在pandas中使用Concat
import pandas as pd      
data1 = pd.Series([0,1,2],index=['A','B','C'])
data2 = pd.Series([3,4],index=['D','E'])
data3 = pd.concat([data1,data2])
print(data3)

在上面的例子中，我们分别创建了两个没有重复Index的Series,
然后用concat默认的把它们合并在一起，这时生成的依然是Series类型
如果我们把axis换成1，那生成的就是Dataframe,像下面一样

data4 = pd.concat([data1,data2],axis=1,sort=True) # sort=Ture是默认的，pandas总是默认index排序，默认axis=0
print(data4)

# 要在相接的时候再加上一个层次的key来识别数据源来自哪张表，可以增加key
result = pd.concat(frames,keys=['df1','df2','df3'])
print(result)

# append
append是series和dataframe的方法，使用它就是默认沿着列进行凭借（axis = 0，列对齐）
result = df1.append(df2)

如果两个表的index都没有实际含义，使用ignore_index参数，置true，合并的两个表就是根据列字段对齐，然后合并。最后再重新整理一个新的index。
result = pd.concat([df1,df4],axis=0,ignore_index=True)
print(result)

# 前面提到的keys参数可以用来给合并后的表增加key来区分不同的表数据来源
# 1.可以直接用key参数实现

result = pd.concat(frames,keys=['x','y','z'])
print(result)

# 2.传入字典来增加分组键
pieces = {'x':df1,'y':df2,'z':df3}
result = pd.concat(pieces)
print(result)


# append方法可以将 series 和 字典就够的数据作为dataframe的新一行插入。
s2 = pd.Series(['X0', 'X1', 'X2', 'X3'], index=['A', 'B', 'C', 'D'])

result = df1.append(s2, ignore_index=True)

# 表格列字段不同的表合并
如果遇到两张表的列字段本来就不一样，但又想将两个表合并，其中无效的值用nan来表示。那么可以使用ignore_index来实现
dicts = [{'A': 1, 'B': 2, 'C': 3, 'X': 4}, {'A': 5, 'B': 6, 'C': 7, 'Y': 8}]
result = df1.append(dicts, ignore_index=True)

# 汇总
concat：可以沿一条轴将多个对象连接到一起
merge：可以根据一个或多个键将不同的DataFrame中的行连接起来。
join：inner是交集，outer是并集。

# 填充
填充常用类型数据
1. pd.read_excel参数：
skiprows = 行数  跳过几行
usecols = '区域' 和Excel中一样，就是一个列的区域
index_col = '字段名' 将谁设置为索引
dtype = {'序号':str,'性别':str,'日期':str}   # 防止出错，把类型全指定为字符型

2. 数据.at的用法
作用：获取某个位置的值，例如，获取第0行，第a列的值，即：index=0，columns='a'
变量名 = 数据.at[0, 'a']

3.日期模块 datetime

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


# 但是月的累计很麻烦，因为累加到12月就要进1位到年份上
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


# 以上的方法是先拿到Series再改值，下面的方法是在DataFrame上直接改值
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






