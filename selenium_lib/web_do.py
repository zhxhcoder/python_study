from selenium import webdriver

# chrome://version/  查询Chrome版本 安装与浏览器版本匹配的webdriver 80.0.3987.122
# http://chromedriver.storage.googleapis.com/index.html下载
# 解压后放到usr/local/bin
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')