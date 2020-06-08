import re
import urllib

from pyquery import PyQuery as pq

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36', }


def get_pages(pageUrl, regex, urlHost):
    res = pq(pageUrl, headers=headers)
    # print(res) # 输出整个html
    href_list = res('a')
    print(href_list)  # 输出所有的<a href="https://www.ivsky.com">天堂图片网</a><a href="/">首页</a>
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

    ###################################################
    imgHeaders = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=C5679A406E2621921D0BE71BE1AD0D0C; UM_distinctid=1646dc3e27910d6-0418aa21b7679c-47e1039-1fa400-1646dc3e27a41b; CNZZDATA1265204377=1796871560-1510557120-%7C1510557120; _cnzz_CV1265204377=BrowserInfo%7CChrome%2F67.0.3396.99%7C0',
        'DNT': '1',
        'Host': 'www.baidu.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    all_img_list = ["http://www.open-open.com/bbs/uploadImg/20160107/20160107133856_341.jpg"]

    for i in range(len(all_img_list)):
        path = "/var/pic/" + str(i) + ".jpg"
        data = urllib.request.urlretrieve(all_img_list[i], path)


if __name__ == "__main__":
    main()
