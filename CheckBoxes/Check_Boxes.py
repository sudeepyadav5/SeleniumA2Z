import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# 1. Find the Lists of Radio Buttons using locator
checkBoxs = driver.find_elements(By.XPATH, "//input[@name='checkbox']")

# 2. Using for loop iterate the object and click on the option
for checkBox in checkBoxs:
    checkBoxText = checkBox.get_attribute("value")
    print(checkBoxText)
    if checkBoxText == "c2":
        checkBox.click()
        print("Check Box Selected", checkBox.is_selected())