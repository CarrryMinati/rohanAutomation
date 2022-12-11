import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class screenshot():
    def takescreenshot(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()


        picture = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")

        picture.screenshot(".//text.png")
        picture.click()
        time.sleep(2)
        driver.get_screenshot_as_file(".\\error.png")

        time.sleep(2)
        driver.save_screenshot(".\\text1.png")
        time.sleep(2)

save = screenshot()
save.takescreenshot()
