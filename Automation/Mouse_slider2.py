import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class slider():
    def mouseslider2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.globalsqa.com/demo-site/sliders/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']"))

        #xsxis run right to left
        xaxis = driver.find_element(By.XPATH, "//div[@id='red']//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
        scxaxis = driver.find_element(By.XPATH, "//div[@id='green']//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
        ActionChains(driver).drag_and_drop_by_offset(scxaxis, -40,0).perform()
        ActionChains(driver).drag_and_drop_by_offset(xaxis, -50, 0).perform()
        time.sleep(3)

demoslider=slider()
demoslider.mouseslider2()