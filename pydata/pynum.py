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
print(d1.describe())  # 一次性输出多个描述性统计指标


def status(x):
    return pd.Series([x.count(), x.min(), x.idxmin(), x.quantile(.25), x.median(),
                      x.quantile(.75), x.mean(), x.max(), x.idxmax(), x.mad(), x.var(),
                      x.std(), x.skew(), x.kurt()], index=['总数', '最小值', '最小值位置', '25%分位数',
                                                           '中位数', '75%分位数', '均值', '最大值', '最大值位数', '平均绝对偏差', '方差', '标准差',
                                                           '偏度', '峰度'])


df = pd.DataFrame(status(d1))
print(df)
print("########################加载CSV数据####################")

bank = pd.read_csv("/data/bank-additional-train.csv")
bank.head()  # 查看前5行

print("########################多表连接####################")
student = {'Name': ['Bob', 'Alice', 'Carol', 'Henry', 'Judy', 'Robert', 'William'],
           'Age': [12, 16, 13, 11, 14, 15, 24],
           'Sex': ['M', 'F', 'M', 'M', 'F', 'M', 'F']}

score = {'Name': ['Bob', 'Alice', 'Carol', 'Henry', 'William'],
         'Score': [75, 35, 87, 86, 57]}

df_student = pd.DataFrame(student)
print(df_student)

df_score = pd.DataFrame(score)
print(df_score)

# 内连接
stu_score1 = pd.merge(df_student, df_score, on='Name')
print(stu_score1)
# 左连接
stu_score2 = pd.merge(df_student, df_score, on='Name', how='left')
print(stu_score2)
