# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 14:00:03 2022

@author: 15517
"""

# 后期我们会接触到机械学习，人工智能，神经网络
# 机械学习中的分箱处理
# 在机械学习中，我们经常会对数据进行分箱处理的操作， 
# 也就是 把一段连续的值切分成若干段，每一段的值看成一个分类。
# 这个把连续值转换成离散值的过程，我们叫做分箱处理。
# 比如，把年龄按15岁划分成一组，0-15岁叫做少年，16-30岁叫做青年，31-45岁叫做壮年。在这个过程中，我们把连续的年龄分成了三个类别，“少年”，“青年”和“壮年”就是各个类别的名称，或者叫做标签。

# cut和qcut函数的基本介绍
# 在pandas中，cut和qcut函数都可以进行分箱处理操作。
# 其中cut函数是按照数据的  值  进行分割，
# 而qcut函数则是根据数据本身的  数量  来对数据进行分割。


pandas.cut(x, bins, right=True, labels=None, retbins=False, precision=3, include_lowest=False)
# 参数：
# 1. x，类array对象，且必须为一维，待切割的原形式
# 2. bins, 整数、序列尺度、或间隔索引。如果bins是一个整数，它定义了x宽度范围内的等宽面元数量，但是在这种情况下，x的范围在每个边上被延长1%，以保证包括x的最小值或最大值。如果bin是序列，它定义了允许非均匀bin宽度的bin边缘。在这种情况下没有x的范围的扩展。
# 3. right,布尔值。是否是左开右闭区间
# 4. labels,用作结果箱的标签。必须与结果箱相同长度。如果FALSE，只返回整数指标面元。
# 5. retbins,布尔值。是否返回面元
# 6. precision，整数。返回面元的小数点几位
# 7. include_lowest，布尔值。第一个区间的左端点是否包含
# 返回值：
# 若labels为False则返回整数填充的Categorical或数组或Series
# 若retbins为True还返回用浮点数填充的N维数组

# pandas.qcut
# pandas.qcut(x, q, labels=None, retbins=False, precision=3, duplicates='raise')
# 参数：
# 1.x 
# 2.q,整数或分位数组成的数组。 
# 3.labels, 
# 4.retbins 
# 5.precisoon 
# 6.duplicates
# 结果中超过边界的值将会变成NA


# 17.1 指定分界点分箱【cut】
import pandas as pd
year = [1992,1983,1922,1932,1973] #待分箱数据
box = [1900,1950,2000] #指定箱子分界点
result = pd.cut(year,box)
print(result)
# 结果说明：其中(1950, 2000]说明【年份】列表的第一个值1992位于(1950, 2000]区间

print(pd.value_counts(result))


# labels参数为False时，返回结果中用不同的整数作为箱子的指示符
结果2 = pd.cut(year, box,labels=False)
# 输出结果中的数字对应着不同的箱子
print(结果2)
# 结果说明：其中 1 说明【year】列表的第一个值1992位于(1950, 2000]区间
# 其中 0 说明【年份】列表的第一个值1922位于(1900, 1950]区间

print(pd.value_counts(结果2))   # 对不同箱子中的数进行计数



import pandas as pd
年份 = [1992, 1983, 1922, 1932, 1973]   # 待分箱数据
箱子 = [1900,  1950,  2000]   # 指定箱子的分界点
# 可以将想要指定给不同箱子的标签传递给labels参数
箱子名称 = [ '50年代前', '50年代后']
结果3 = pd.cut(year,box, labels=箱子名称)
print(pd.value_counts(结果3))


# 17.2 等频分箱 【qcut】
import pandas as pd
年份 = [1992, 1983, 1922, 1932, 1973, 1999, 1993, 1995]   # 待分箱数据
结果 = pd.qcut(年份,q=4)   # 参数q指定所分箱子的数量
# 从输出结果可以看到每个箱子中的数据量时相同的
print(结果)
print(pd.value_counts(结果))  # 从输出结果可以看到每个箱子中的数据量时相同的

































