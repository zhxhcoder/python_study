import pandas as pd

filescv = pd.read_csv("sss.csv")
filescv.to_excel('sss' + '.xlsx', encoding='gbk')
