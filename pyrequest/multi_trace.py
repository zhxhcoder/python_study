import time

import pandas as pd


# 装饰器，打印函数的执行时间
def gettime(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print(func.__name__, 'Start...')
        starttime = time.time()
        func(*args)
        endtime = time.time()
        spendtime = endtime - starttime
        print(func.__name__, "End...")
        print("Spend", spendtime, "s totally")
        print("=" * 50)

    return wrapper()


# 从文件取n个网址测试

def get_urls_from_file(n):
    df = pd.read_csv('TestUrls.csv')  # 共1000个网址
    urls = list(df['url'][:n])
    return urls

# 请求并解析网页获取数据
