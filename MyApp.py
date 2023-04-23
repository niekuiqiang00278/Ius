#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 3:38
# @Author  : cap669
# @File    : MyApp.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
class MyApp:
    def __init__(self, executable_path=r"C:\Kac\Tool\chromedriver.exe"):
        options = Options()
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        service = Service(executable_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        print(self.driver.title)
        # self.driver.close()
        # self.driver.quit()
if __name__ == '__main__':
    MyApp()

# Tips     :
