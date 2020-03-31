import concurrent
import threading
import time
from concurrent import futures
from multiprocessing import Pool

import pandas as pd
import requests


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
def getdata(url, retries=3):
    # print("正在下载：",url)
    headers = {}
    try:
        html = requests.get(url, headers=headers)
        # print(html)
    except requests.exceptions.ConnectionError as e:
        # print('下载出错[ConnectError:',e)
        html = None
    # 5xx错误为服务器错误，可以重新进行请求
    if (html != None and 500 <= html.status_code < 600 and retries):
        retries -= 1
        print('服务器错误正在重试...')
        getdata(url, retries)
        data = html.text
    else:
        data = None
    return None


# 串行
@gettime
def Dnormal(urls):
    for url in urls:
        getdata(url)


# 进程池
@gettime
def DprocessPool(urls, num=10):
    pool = Pool(num)
    results = pool.map(getdata, urls)
    pool.close()
    pool.join()
    return results


# 多线程
@gettime
def Dmultithread(urls, max_threads=10):
    def urls_process():
        while True:
            try:
                url = urls.pop()
            except IndexError:
                break
            data = getdata(url, retries=3)

    threads = []
    # 未达到最大线程限制且仍然存在待爬取的url时，可以创建新的线程进行加速
    while int(len(threads) < max_threads) and len(urls):
        thread = threading.Thread(target=urls_process)
        print('创建线程', thread.getName())
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


# 线程池
@gettime
def Dfutures(urls, num_of_max_works=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_max_works) as executor:
        executor.map(getdata, urls)


if __name__ == '__main__':
    urls = get_urls_from_file(100)
    Dnormal(urls)
    DprocessPool(urls)
    Dmultithread(urls)
    Dfutures(urls)
