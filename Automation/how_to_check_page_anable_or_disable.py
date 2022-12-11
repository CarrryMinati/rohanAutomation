import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class find_unable_or_disable():
    def findelement(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://login.mailchimp.com/?_ga=2.184555625.1398121277.1660041267-1467270392.1660041267&_gac=1.54545881.1660041267.CjwKCAjwi8iXBhBeEiwAKbUofVwbpR3E4K-X2b_sATRcNHxSFeE9QSQBOL4Ef3SpwYypEtJ45XYSzhoCQHoQAvD_BwE")
        enabletext1 = driver.find_element(By.XPATH, "//*[@id='submit-btn']").is_enabled()
        print(enabletext1)



        driver.find_element(By.XPATH,"//input[@id='username']").send_keys("roahnspatl2229@gmail.com")
        driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Rohan@123")
        enabletext = driver.find_element(By.XPATH,"//*[@id='submit-btn']").is_enabled()
        print(enabletext)

        enabletext1 = driver.find_element(By.XPATH, "//*[@id='submit-btn']").is_enabled()
        print(enabletext1)



UD= find_unable_or_disable()
UD.findelement()