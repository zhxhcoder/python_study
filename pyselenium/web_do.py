from selenium import webdriver

# chrome://version/  查询Chrome版本 安装与浏览器版本匹配的webdriver
# http://chromedriver.storage.googleapis.com/index.html下载
# 解压后放到usr/local/bin


options = webdriver.ChromeOptions()  # 设置存储浏览器的信息
#  添加代理服务器
options.add_argument("--proxy-server=http://110.73.2.248:8123")

browser = webdriver.Chrome(chrome_options=None)
browser.get('https://www.baidu.com/')
# print(browser.page_source)


# 获取所有的cookie：
for cookie in browser.get_cookies():
    print(cookie)

# browser.close()  # 关闭当前页面。browser.quit() 退出整个浏览器
