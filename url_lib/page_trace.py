import re
import requests
import urllib

from pyquery import PyQuery as pq

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0', }


def get_root_page(pageUrl):
    res = pq(url, headers=headers)
    # print(res) # 输出整个html
    href_list = res('a')
    # print(href_list)  # 输出所有的<a href="https://www.ivsky.com">天堂图片网</a><a href="/">首页</a>
    regex = re.compile(r'/tupian/\w+/pic.+\.html')  # 匹配子html
    page_list = []
    for q in href_list.items():
        # print(q)  # <a href="/about/disclaimer.html" rel="nofollow">免责声明</a>
        href_value = q.attr('href')
        # print(q1) # /about/disclaimer.html
        m = regex.match(str(href_value))
        if m:
            page_list.append(href_value)
            page_list = list(set(page_list))  # list元素去重
    # for each in page_list:
    #     print(each)
    return page_list


for i in range(1, 20):
    url = "https://www.ivsky.com/tupian/meinv_t50/index_" + str(i) + ".html"
    print(url)
    print('第%s页抓到%d个大图首页' % (i, len(get_root_page(url))))
