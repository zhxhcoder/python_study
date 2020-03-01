import re
import requests
import urllib

from pyquery import PyQuery as pq

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0', }


def get_pages(pageUrl, regex, urlHost):
    res = pq(pageUrl, headers=headers)
    # print(res) # 输出整个html
    href_list = res('a')
    # print(href_list)  # 输出所有的<a href="https://www.ivsky.com">天堂图片网</a><a href="/">首页</a>
    page_list = []
    for q in href_list.items():
        # print(q)  # <a href="/about/disclaimer.html" rel="nofollow">免责声明</a>
        href_value = q.attr('href')
        # print(href_value) # /about/disclaimer.html
        m = regex.match(str(href_value))
        if m:
            page_list.append(urlHost + href_value)
            page_list = list(set(page_list))  # list元素去重
    # for each in page_list:
    #     print(each)
    return page_list


def get_imgs(pageUrl, regex, urlHost):
    res = pq(pageUrl, headers=headers)
    # print(res) # 输出整个html
    img_list = res('img')
    # print(img_list)  # <img id="imgis" src="//img.ivsky.com/img/tupian/pre/20
    page_list = []
    for q in img_list.items():
        # print(q)  # <img src="//img.ivsky.com/img/tupian/m/201809/24/shishang_sheying-004.jpg" alt="&#x65F6;&#x5C1A;&#x6444;&#x5F71;&#x56FE;&#x7247;"/>
        img_value = q.attr('src')
        # print(href_value)  # //img.ivsky.com/img/tupian/pre/201909/13/huahuan_meinv-009.jpg
        m = regex.match(str(img_value))
        if m:
            page_list.append(urlHost + img_value)
            page_list = list(set(page_list))  # list元素去重
    for each in page_list:
        print(each)
    return page_list


def main():
    ###################################################
    all_pages = []

    for i in range(1, 2):
        url = "https://www.ivsky.com/tupian/meinv_t50/index_" + str(i) + ".html"
        print(url)

        url_pages = get_pages(url, re.compile(r'/tupian/\w+/pic.+\.html'), "https://www.ivsky.com")
        print('第%s页抓到%d个大图首页' % (i, len(url_pages)))
        all_pages += url_pages

    all_pages = list(set(all_pages))

    ###################################################
    all_imgs = []

    for page in all_pages:
        url_imgs = get_imgs(page, re.compile(r'/.+\.jpg'), "https://www.ivsky.com")
        all_imgs += url_imgs

    all_imgs = list(set(all_imgs))

    for each in all_imgs:
        print(each)


if __name__ == "__main__":
    main()
