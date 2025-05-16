from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import datetime

def web_set():
    op = Options()
    op.add_argument('--no-sandbox')   # 禁用沙盒
    op.add_experimental_option('detach', True)
    dev = webdriver.Edge(options=op)
    dev.maximize_window()
    return dev
url_1 = ''
url_2 = ''

web = web_set()
web.get(url_1)
web.implicitly_wait(1)
web.find_element(By.NAME, 'account').send_keys('账号')
web.find_element(By.NAME, 'password').send_keys('密码')
web.find_element(By.CLASS_NAME, 'ant-checkbox-input').click()
web.find_elements(By.TAG_NAME, 'button')[1].click()
time.sleep(1)
web.get(url_2)
web.implicitly_wait(1)
web.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div/div/a[1]').click()
web.implicitly_wait(2)
KK = True
while KK:
    now = datetime.datetime.now()
    print(now)
    if now.strftime('%Y-%m-%d %H:%M:%S') == '2025-03-17 20:00:00':
        for i in range(10):
            # 购买按钮的Xpath
            web.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[1]/div[2]/div[6]/div[1]/a').click()
            # web.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[1]/div[2]/div[6]/div[2]/a').click()  # 喜欢
            print('已点击')
        KK = False

    time.sleep(0.01)  # 注意刷新间隔时间要尽量短




