import os
import re
import time
from threading import Thread

import pymysql
import requests
from pyquery import PyQuery as pq


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

    for i in range(1, 215):
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

    ###################################################

    # 创建连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='db_zhu',
                           charset='UTF8MB4')
    # 创建游标
    cursor = conn.cursor()
    # 创建表
    sql_create_table = '''CREATE TABLE `guochan`(
      `id` INT NOT NULL AUTO_INCREMENT,
      `url` CHAR(200) ,
      `time` TIME,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;
    '''
    cursor.execute(sql_create_table)

    sql_insert = "INSERT INTO guochan(url, time) VALUES (%s, %s);"

    try:
        for i in range(len(all_imgs)):
            print("imageUrl", all_imgs[i])
            cursor.execute(sql_insert, [all_imgs[i], time.strftime("%Y-%m-%d %H:%M:%S")])
            # DownloadHandler(all_imgs[i]).start()
    except:
        # 出现错误 就回滚
        conn.rollback()

    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()


if __name__ == "__main__":
    main()
