# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:31:37 2022

@author: 15517
"""

# 1.datatime模块中定义的类
datetime.date # 表示日期，常用属性有：year,month 和 day
datetime.time # 表示时间,常用属性有： hour,minute,second,microsecond
datetime.timedelta #表示两个date、time、datetime之间的时间间隔
datetime.tzinfo  #时区相关信息对象的抽象基类，他们由datetime和time类使用，提供自定义时间的调整
datetime.timezone 

# 2.datetime模块中的常量
datetime.MINYEAR #datetime.date 或 datetime.datetime对象所允许的年分的最小值,值为1
datetime.MAXYEAR #datetime.date 或 datetime.datetime对象所允许的年分的最大值,值为9999

# 3.对象方法和属性
d.year
d.month
d.day
d.replace(year[,month[,day]]) #生成并返回一个新的日期对象，原日期对象不变
d.timetuple()  #返回日期对应的time.struct_time对象
d.toordinal()  #返回日期是自0001-01-01开始的第多少天
d.weekday()    #返回日期是星期几，[0,6],0表示星期一
d.isoweekday() #返回日期是星期几，[1,7]
d.isocalendar()#返回一个元组，格式为(year,month,isoweekday)
d.isoformat()  #返回'YYYY-MM-DD'格式的日期字符串
d.strftime(format) #返回指定格式的日期字符串


# 4.datetime.time类
# time类的定义
class datetime.time(hour,[minute[,second,[microsecond[,tzinfo]]]]):
# hour为必须参数，其他参数可选，可参数的范围为：
# hour  [0,23]
# minute [0,59]
# second [0,59]
# microsecond [0,1000000]
# tzinfo  tzinfo的子类对象，如timezone类的实例

# 类方法和属性
time.max  #time类所能表示的最大时间：time(23,59,59,999999)
time.min  #time类所能表示的最小时间：time(0,0,0)
time.resolution #时间的最小单位，即两个不同时间的最小差值：1微秒

# 对象方法和属性
t.hour 
t.minute
t.second
t.microsecond
t.tzinfo  #返回传递给time构造方法的tzinfo对象，如果该参数未给出则返回None
t.replace(hour[,minute[,second[,microsecond[,tzinfo]]]])
t.isoformat()  #返回一个'HH:MM:SS.%f'格式的时间字符串
t,strftime()   #返回指定格式的时间字符串

























