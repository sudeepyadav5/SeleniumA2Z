import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# 1. Find the Lists of Radio Buttons using locator
radiobtns = driver.find_elements(By.XPATH, "//input[@name='radio']")

# 2. Using for loop iterate the object and click on the option
for radiobtn in radiobtns:
    radiobtntext = radiobtn.get_attribute("value")
    print(radiobtntext)
    if radiobtntext == "Button3":
        radiobtn.click()
        print("Radio Button is Selected", radiobtn.is_selected())
        break
