import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://www.dummypoint.com/seleniumtemplate.html")

# 1. Find the Lists of Radio Buttons using locator
dd_Element = driver.find_element(By.ID, "multiselect")

# Create Object for Select Class
multiselect_options = Select(dd_Element)

print("Check whether it is Multi Select or not ", multiselect_options.is_multiple)

# List the value of Multi Select
multiselect_values = multiselect_options.options

for multiselect_value in multiselect_values:
    print(multiselect_value.text)


time.sleep(2)
print("------------------Selected---------------------")

# Select By Index
multiselect_options.select_by_index(2)
time.sleep(3)

# Select By Value
multiselect_options.select_by_value("mOptionFour")
time.sleep(3)

# Select By Text
multiselect_options.select_by_visible_text("mOption5")
time.sleep(3)

print("------------------DiSelected---------------------")

# Select By Index
multiselect_options.deselect_by_index(2)
time.sleep(3)

# Select By Value
multiselect_options.deselect_by_value("mOptionFour")
time.sleep(3)

# Select By Text
multiselect_options.deselect_by_visible_text("mOption5")

print("------------------Selected---------------------")

# Select By Index
multiselect_options.select_by_index(2)
time.sleep(3)

# Select By Value
multiselect_options.select_by_value("mOptionFour")
time.sleep(3)

# Select By Text
multiselect_options.select_by_visible_text("mOption5")
time.sleep(3)

print("------------------DeSelected---------------------")
multiselect_options.deselect_all()

time.sleep(5)
driver.quit()