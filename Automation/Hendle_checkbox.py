#ERROR IN CODE SOLWE AFTER SOME TIME




import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class HandleCheckBox():
    def vreifycheckbox(self):
         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
         driver.get("https://www.yatra.com/flights")
         driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']//i[@class='ico ico-checkbox']").click()
         time.sleep(4)
         print(driver.find_element(By.XPATH, "//a[@title='Non Stop Flights']").is_selected())
HC = HandleCheckBox()
HC.vreifycheckbox()


'''class HandleCheckBox():
    def vreifycheckbox(self):
         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
         driver.get("https://www.functionize.com/h/test-automation?utm_source=google&utm_medium=paid%20search&utm_campaign=automated%20web%20testing&utm_term=automated%20web%20testing&utm_campaign=Z+-+India+-+Automated+Web+Testing&utm_source=adwords&utm_medium=ppc&hsa_acc=5488573823&hsa_cam=16375912712&hsa_grp=133300773506&hsa_ad=583785827758&hsa_src=g&hsa_tgt=kwd-304942589907&hsa_kw=automated%20web%20testing&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwrs2XBhDjARIsAHVymmRz3m6Q-wa-oEZ8hid40vT6HUGf-yi8WRcCcJ1q3SiTbHv8qVo3fXAaAlMQEALw_wcB")
         driver.find_element(By.XPATH,"//input[@id='terms_and_conditions-e65821c3-a1ec-4b15-9767-25c917c9afc1']").click()
         driver.maximize_window()
         time.sleep(100)
        # check = driver.find_element(By.XPATH, "//input[@id='interest_market_c0']").is_selected()
        # print(check)

DG= HandleCheckBox()
DG.vreifycheckbox()
'''
