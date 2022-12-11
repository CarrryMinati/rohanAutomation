

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Explicitly():
    def Exwait(self):
        driver =webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@name='login-input']").send_keys("rohan")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "login-continue-btn"))).click()
        driver.find_element(By.ID, "login-continue-btn").click()



Explit = Explicitly()
Explit.Exwait()
