#find element using HTML tags and enter some valid data.
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class findelementbytagname():
    def located_by_tag(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.TAG_NAME, "input").send_keys("rohanspatil2229@gmail.com")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(90.0)

sd=findelementbytagname()
sd.located_by_tag()
