import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class newelements():
    def elements(self):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        lista=driver.find_elements(By.TAG_NAME, "a")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(5.0)

fa=newelements()
fa.elements()