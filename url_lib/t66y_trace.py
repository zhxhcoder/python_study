import re
import requests
from bs4 import BeautifulSoup


# 第一步得到代理
def proxy():
    with open(r'ip_proxies\有效ip.txt', 'r', encoding='utf-8') as f:
        r = f.readlines()
        for ip in r:
            try:
                proxies = eval(ip)
                if requests.get('http://t66y.com/index.php', proxies=proxies, timeout=2).status_code == 200:
                    return proxies
            except:
                pass


proxies = proxy()
print(proxies)

# 第二步得到网页链接池
url = 'http://t66y.com/index.php'
url2 = 'http://t66y.com/thread0806.php?fid=16'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,\
image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
session = requests.session()
url_response = session.get(
    url, headers=headers, proxies=proxies, timeout=3)
url_response2 = session.get(url2, timeout=3, proxies=proxies)
data = url_response2.content.decode('gbk', 'ignore')
soup = BeautifulSoup(data, features='lxml')
url_list = soup.find_all(href=re.compile("htm_data"))
url_set = set()
for i in url_list:
    try:
        url_final = 'http://t66y.com/' + i['href']
        url_set.add(url_final)
    except:
        pass

# 第三步抓取当前页的图片
n = 1


def get_jpg(url):
    global n
    response = requests.get(url, headers=headers, proxies=proxies)
    print(response.status_code)
    data = response.content.decode('gb2312', 'ignore')
    soup = BeautifulSoup(data, features='lxml')
    inputs = soup('input')
    for i in inputs:
        try:
            url_jpg = i['data-src']
            jpg = requests.get(url_jpg, headers=headers, timeout=5)
            print('第{}张'.format(n))
            jpg_content = jpg.content
            with open(r'Caoliu photo\{}.jpg'.format(n), 'wb') as f:
                f.write(jpg_content)
                print('完成')
                n = n + 1
        except Exception as a:
            print(a)


if __name__ == "__main__":
    url_final_list = list(url_set)
    for i in url_final_list:
        print(i)
        get_jpg(i)
