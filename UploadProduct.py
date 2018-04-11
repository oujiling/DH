import sys
import io
from selenium import webdriver
from urllib import request
import re
import time
import json
from lxml import etree

# 初次建立连接，随后方可修改cookie
browser = webdriver.Chrome()
browser.get('http://seller.dhgate.com')
# 删除第一次建立连接时的cookie
browser.delete_all_cookies()
# 读取登录时存储到本地的cookie
with open('cookies.json', 'r', encoding='utf-8') as f:
    listCookies = json.loads(f.read())
for cookie in listCookies:
    browser.add_cookie({
        'domain': '.dhgate.com',  # 此处xxx.com前，需要带点
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })
# 再次访问页面，便可实现免登陆访问
productUrl = "https://www.dhgate.com/product/waiter-s-wine-tool-bottle-opener-sea-horse/84552683.html"
html = request.urlopen(productUrl).read()
tree = etree.HTML(html)
catepubid = re.findall('_pro_catepubid="(.*?)";', str(html))[0]
cpbt = tree.xpath("//div[@class='hinfo clearfix']/h1")[0].text

uploadUrl = "http://seller.dhgate.com/syi/edit.do?jsversion=20170710&cssversion=1523155457271&inp_catepubid=%s" % catepubid
browser.get(uploadUrl)
browser.get("http://seller.dhgate.com/mydhgate/product/productentry.do?act=edit")
cpbt_in = browser.find_element_by_xpath("//input[@id='productname']")
cpbt_in.send_keys('yenvine')
browser.implicitly_wait(3)
time.sleep(300)
