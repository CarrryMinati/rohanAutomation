import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
try:
    class find_text():
      def findtext(self):
          driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
          driver.get("https://www.yatra.com/")
          driver.maximize_window()
          text=driver. find_element(By.XPATH, "(//span[contains(text(),'Domestic Flights')])[1]").text
          text1=driver. find_element(By.LINK_TEXT, "Yatra for Business").text
          print(text)
          print(text1)
          time.sleep(3)
except Exception as e:
    print(e)

else:
    print("good")

find = find_text()
find.findtext()