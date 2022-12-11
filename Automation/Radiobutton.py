#CORRECT REDOBUTTON PROGRAM
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class redio():
    def rediobutton(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(4)
        print( driver.find_element(By.ID, "doi0").is_selected())
        driver.find_element(By.ID,"doi0").click()
        time.sleep(4)
        print(driver.find_element(By.ID, "doi0").is_selected())
        driver.find_element(By.ID,"doi1").click()
        print(driver.find_element(By.ID, "doi0").is_selected())
        print(driver.find_element(By.ID, "doi1").is_selected())
        time.sleep(4)
call = redio()
call.rediobutton()