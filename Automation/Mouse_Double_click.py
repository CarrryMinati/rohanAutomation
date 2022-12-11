import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class double():
    def doubleclick(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        store = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction()']")
        ActionChains(driver).double_click(store).perform()
        time.sleep(3)

rohan = double()
rohan.doubleclick()