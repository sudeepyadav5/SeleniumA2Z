import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(2)

driver.get("http://www.dummypoint.com/Actions.html")
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

time.sleep(5)
driver.quit()