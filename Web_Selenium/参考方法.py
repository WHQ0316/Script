from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

import time

def web_set():
    q1 = Options()
    q1.add_argument('--no-sandbox')   # 禁用沙盒
    q1.add_experimental_option('detach', True)
    a1 = webdriver.Edge(options=q1)
    return a1

url = ''

a1 = web_set()
a1.get('')   # 打开
# time.sleep(2)  # 延迟
# a1.close()                    # 关闭

# a2 = a1.find_element(By.ID, 'kw')
# a2.send_keys('xiaomi')     # 输入
# botten = a1.find_element(By.ID, 'su')
# botten.click()             # 点击
# class定位：：value值不能有空格！！！！！
# TAG_NAME: <标签>
#

