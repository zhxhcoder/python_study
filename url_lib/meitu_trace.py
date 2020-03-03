import os
import re
from threading import Thread

import requests
import urllib

from pyquery import PyQuery as pq

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36', }


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = re.sub(r"https.+img", "", self.url).replace("/", "")
        resp = requests.get(self.url)

        imgDir = '/Users/xhzh/pic/'
        if not os.path.exists(imgDir):
            os.mkdir(imgDir)

        with open(imgDir + filename, 'wb') as f:
            f.write(resp.content)


def get_pages_url(pageUrl, regex, urlHost):
    print(pageUrl, regex, urlHost)  # 输出整个html
    resp = requests.get(pageUrl)
    res = pq(resp.text)
    href_list = res('a')
    page_list = []
    for q in href_list.items():
        href_value = q.attr('href')
        m = regex.match(str(href_value))
        if m:
            finalUrl = urlHost + href_value
            print('第二级页面', finalUrl)
            page_list.append(finalUrl)
            page_list = list(set(page_list))  # list元素去重
    return page_list


def get_imgs_url(pageUrl, regex, urlHost):
    print(pageUrl, regex, urlHost)  # 输出整个html
    resp = requests.get(pageUrl)
    res = pq(resp.text)
    img_list = res('img')
    page_list = []
    for q in img_list.items():
        img_value = q.attr('src')
        m = regex.match(str(img_value))
        if m:
            finalUrl = urlHost + img_value
            print('第三级页面', finalUrl)
            page_list.append(finalUrl)
            page_list = list(set(page_list))  # list元素去重
    for each in page_list:
        print(each)
    return page_list


def main():
    ###################################################
    all_pages = []

    for i in range(1, 2):
        url = "https://www.meitulu.com/guochan/" + str(i) + ".html"
        print('第一级页面', url)

        url_pages = get_pages_url(url, re.compile(r'\/item.+html'), "https://www.meitulu.com")
        print('第%s页抓到%d个大图首页' % (i, len(url_pages)))
        all_pages += url_pages

    all_pages = list(set(all_pages))

    ###################################################
    all_imgs = []

    for page in all_pages:
        url_imgs = get_imgs_url(page, re.compile(r'https.+images.+\.jpg'), "")
        all_imgs += url_imgs

    all_imgs = list(set(all_imgs))

    for i in range(len(all_imgs)):
        DownloadHandler(all_imgs[i]).start()


def test():
    tstUrl = "https://www.meitulu.com/guochan/1.html"
    resp = requests.get(tstUrl)
    res = pq(resp.text)

    href_list = res('a')
    print(href_list)

    pass


if __name__ == "__main__":
    main()
    # test()
    # DownloadHandler("https://mtl.gzhuibei.com/images/img/20713/56.jpg").start()
