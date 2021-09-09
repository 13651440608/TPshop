# 开发人员： 曾祥茂
# 日期： 2021/03/31
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCase:
    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    def test_case(self):
        self.driver.get('http://www.testingedu.com.cn:8000/')
        self.driver.find_element(By.XPATH, '//*[@title="手机"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="ajax_hot_goods"]/div[1]/p[1]/a').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, '//*[@id="buy_now"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="checkout-submit"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="cart4_form"]/div/div/dl/dd/div/div[2]/ul/li[2]/div/label').click()
        self.driver.find_element(By.XPATH, '//*[@id="cart4_form"]/div/div/div/a').click()
