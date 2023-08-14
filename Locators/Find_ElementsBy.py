import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/seleniumtemplate.html")

elements = driver.find_elements(By.ID, "app")
for item in elements:
    print(item.text)

time.sleep(2)
driver.quit()


