# Snapdeal slider program


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class snap():
    def snapdeal(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/search?keyword=mobile%20phones&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
        driver.maximize_window()
        slide = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        slideback =driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(slide, 60, 0).perform()
        time.sleep(3)
        #ActionChains(driver).click_and_hold(slide).pause(2).move_by_offset(60, 0).release().perform()  # thise two way to performe sliders
        #ActionChains(driver).move_to_element(slide).click_and_hold(slide).pause(1).move_by_offset(70, 0).release().perform()

        ActionChains(driver).drag_and_drop_by_offset(slideback, -20, 0).perform()
        time.sleep(3)


slider=snap()
slider.snapdeal()