import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class orange():
    def orangehrm(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://orangehrm.qedgetech.com/symfony/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(2)
        perant_window = driver.current_window_handle
        print("thise is perant window",perant_window)
        driver.find_element(By.XPATH, "//img[@alt='LinkedIn OrangeHRM group']").click()
        time.sleep(2)
        child_window = driver.window_handles
        print("thise is child window ",child_window)
        for child in child_window:
            if perant_window != child:
                driver.switch_to.window(child)
                driver.find_element(By.NAME, "email-or-phone").send_keys("rohansapitl2229@gmail.com")
                time.sleep(2)
                driver.close()
        driver.switch_to.window(perant_window)
        print("preant window title", perant_window)

        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(2)

sd = orange()
sd.orangehrm()
