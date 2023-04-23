import time
from json import load
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from data.config.DataConfig import dataconf


class JesHit:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('debuggerAddress', f'{dataconf.host}:{dataconf.port}')
        self.service = Service(executable_path=dataconf.executable_path)

class JesBis(JesHit):
    def __init__(self):
        JesHit.__init__(self)
    def km1(self):
        f = open(file=r'C:\Kac\Python\Ius\data.json',encoding='UTF-8',mode='r')
        d = load(f)
        f.close()
        return d

    def km0(self,uid:str):
        driver = webdriver.Chrome(service=self.service, options=self.options)
        if driver.current_url[30:38] == uid:
            pass
        else:
            driver.get(f'https://www.netflix.com/watch/{uid}')
            time.sleep(1)
        return driver.execute_script('return window.lln.subManager.data')

    def km2(self,uid):
        if dataconf.clash:
            return self.km0(uid)
        else:
            return self.km1()
if __name__ == '__main__':
    jes = JesBis()
    a0 = jes.km2('70196279')
    print(a0)
