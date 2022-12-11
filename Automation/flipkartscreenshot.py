import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class flipkart():
    def screenshot(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()

        store = driver.find_element(By.XPATH, "//button[@type='submit']//span[contains(text(),'Login')]")
        time.sleep(2)
        store.screenshot(".\\flipkart.png")
        store.click()

        driver.get_screenshot_as_file(".\\flipkartfull.png")
        time.sleep(2)
        driver.save_screenshot(".\\againfull.png")
        time.sleep(2)


take = flipkart()
take.screenshot()