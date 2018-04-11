import sys
import io
from selenium import webdriver
from urllib import request
import re
import time
import json

# 建立Phantomjs浏览器对象，括号里是phantomjs.exe在你的电脑上的路径
browser = webdriver.Chrome()

# 登录页面
loginUrl = r'https://secure.dhgate.com/passport/login'

# 访问登录页面
browser.get(loginUrl)

# 等待一定时间，让js脚本加载完毕
browser.implicitly_wait(3)

# 输入用户名
username = browser.find_element_by_name('username')
username.send_keys('yenvine')

# 输入密码
password = browser.find_element_by_name('password')
password.send_keys('baqiaokejidh')

# 点击“登录”按钮
login_button = browser.find_element_by_name('loginSubmit')
login_button.submit()

# # 网页截图
# browser.save_screenshot('picture1.png')
# # 打印网页源代码
# print(browser.page_source.encode('utf-8').decode())

dictCookies = browser.get_cookies()
jsonCookies = json.dumps(dictCookies)
# 登录完成后，将cookie保存到本地文件
with open('cookies.json', 'w') as f:
    f.write(jsonCookies)
# print(html.decode('utf-8'))


