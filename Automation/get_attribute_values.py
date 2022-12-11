import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class find_attribute_values():
    def findattributevalues(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        atributevalues = driver.find_element(By.XPATH, "//*[@id='BE_flight_flsearch_btn']").get_attribute("id") # we give the HTML attributes
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Hotels']").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.minimize_window()
        print(atributevalues)
        time.sleep(4)

fe=find_attribute_values()
fe.findattributevalues()
