from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class filipkart():
    def find_css_element(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.flipkart.com/")

        driver.find_element(By.CSS_SELECTOR,"input[class='_2IX_2- VJZDxU']").send_keys("rohanspatil2229@gmail.com")
        driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("Rohan@123")
        driver.find_element(By.CSS_SELECTOR,"button[class='_2KpZ6l _2HKlqd _3AWRsL']").click()

        time.sleep(100.0)

fk = filipkart()
fk.find_css_element()



