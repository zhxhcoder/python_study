import numpy as np
import pandas as pd

print("########################随机生成三组数据####################")
np.random.seed(1234)
d1 = pd.Series(2 * np.random.normal(size=10) + 3)
d2 = np.random.f(2, 4, size=10)
d3 = np.random.randint(1, 10, size=10)
print(d1)
print(d2)
print(d3)
print("########################统计分析用到的函数####################")
d1.count()  # 非空元素计算
d1.min()  # 最小值
d1.max()  # 最大值
d1.idxmin()  # 最小值的位置，类似于R中的which.min函数
d1.idxmax()  # 最大值的位置，类似于R中的which.max函数
d1.quantile(0.1)  # 10%分位数
d1.sum()  # 求和
d1.mean()  # 均值
d1.median()  # 中位数
d1.mode()  # 众数
d1.var()  # 方差
d1.std()  # 标准差
d1.mad()  # 平均绝对偏差
d1.skew()  # 偏度
d1.kurt()  # 峰度
d1.describe()  # 一次性输出多个描述性统计指标
