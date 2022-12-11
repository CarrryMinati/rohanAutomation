import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class find():
    def elements(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        moving=driver.find_element(By.XPATH, "//span[@class='more-arr']")
        ActionChains(driver).move_to_element(moving).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Gift Voucher']").click()
        time.sleep(2)

final= find()
final.elements()

