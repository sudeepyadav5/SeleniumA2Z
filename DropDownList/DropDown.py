import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# 1. Find the Lists of Radio Buttons using locator
dd_Element = driver.find_element(By.ID, "dropdown")
dd_Element.click()

# Create Object for Select Class
dd_options = Select(dd_Element)

# List the value of DropDrop
dd_values = dd_options.options

for dd_value in dd_values:
    print(dd_value.text)

time.sleep(2)

# Select By Index
dd_options.select_by_index(2)
time.sleep(3)

# Select By Value
dd_options.select_by_value("OptionFour")
time.sleep(3)

# Select By Text
dd_options.select_by_visible_text("Option3")



time.sleep(5)
driver.quit()