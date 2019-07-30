# -*- coding: utf8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

driver = webdriver.Chrome('/Users/jeongnamjin/Desktop/YSCEC_selenium/chromedriver')
driver.implicitly_wait(3)

driver.get('https://yscec.yonsei.ac.kr')

driver.find_element_by_name('username').send_keys('your id')
driver.find_element_by_name('password').send_keys('your pw')

driver.find_element_by_id('loginbtn').click()

driver.get('https://yscec.yonsei.ac.kr/local/courselist/courseoverview.php')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

notices_content = soup.select('div.course_list > div > div.activity_info1 > div')
notices_title = soup.select('div.course_list > div > div > h2 > a')

a = []
b = []

for n1 in notices_title:
  a.append(n1.text.strip())

for n2 in notices_content:
  b.append(n2.text.strip())

group_data = OrderedDict()

for i in range(len(a)):
  group_data[a[i]] = b[i]

print(a)
