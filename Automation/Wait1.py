from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class whatsapp():
    def what(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.linkedin.com/signup")
        driver.implicitly_wait(10) # if any arror in program than thise method wait for 10 sec
        driver.find_element(By.ID, "email-or-phone").send_keys("rohan")
whatsappwait = whatsapp()
whatsappwait.what()