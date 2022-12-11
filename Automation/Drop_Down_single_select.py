import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select             # IMPORT SELECT

class Dropdownsingleselect():
    def  dropdawn(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/")
        jobtitle = driver.find_element(By.NAME, "UserTitle")      # WE DON'T SEND ANY KEY (STORE VALUE IN JOBTITLE LOCATER )
        drop_and_dawn  = Select(jobtitle)

        employeers = driver.find_element(By.NAME, "CompanyEmployees")
        drop_and_dawn1 = Select(employeers)

       #JOBTITLE DROPDAWN
        drop_and_dawn.select_by_index(1)                           #in select feature there are three types of you select value "byindex", byvalue", "byvisible_text"
        time.sleep(3)

        drop_and_dawn.select_by_value("Customer_Service_Manager_ANZ")
        time.sleep(3)

        drop_and_dawn.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)

      # EMPLOYEER DROP DAWN
        drop_and_dawn1.select_by_index(2)
        time.sleep(3)
        drop_and_dawn1.select_by_value("250")
        time.sleep(3)
        drop_and_dawn1.select_by_visible_text("2001+ employees")
        time.sleep(3)



DrDo= Dropdownsingleselect()
DrDo.dropdawn()


