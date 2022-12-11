import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Mouse():
    def mouseactons(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        chain = ActionChains(driver)
        mouseaction = driver.find_element(By.XPATH, "//span[@class='more-arr']")

        chain.move_to_element(mouseaction).perform()
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(3)

Actionmouse = Mouse()
Actionmouse.mouseactons()